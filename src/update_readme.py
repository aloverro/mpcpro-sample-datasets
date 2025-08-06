#!/usr/bin/env python3
"""
update_readme.py

Updates the repository's README.md file with an up-to-date listing of all datasets under the 'datasets' directory.

Usage:
    python src/update_readme.py [--branch BRANCH]
    python src/update_readme.py -h|--help
"""
import os
import sys
import argparse
import json
import subprocess
from pathlib import Path

def get_git_info():
    # Get username and repo name from git remote
    try:
        remote_url = subprocess.check_output([
            'git', 'config', '--get', 'remote.origin.url'
        ], encoding='utf-8').strip()
        if remote_url.startswith('git@'):
            # git@github.com:owner/repo.git
            _, path = remote_url.split(':', 1)
            owner, repo = path.split('/', 1)
        elif remote_url.startswith('https://'):
            # https://github.com/owner/repo.git
            parts = remote_url.split('/')
            owner = parts[-2]
            repo = parts[-1]
        else:
            raise Exception('Unknown git remote url format')
        repo = repo.removesuffix('.git')
    except Exception as e:
        print(f"Error getting git remote info: {e}")
        sys.exit(1)
    # Get current branch
    try:
        branch = subprocess.check_output([
            'git', 'rev-parse', '--abbrev-ref', 'HEAD'
        ], encoding='utf-8').strip()
    except Exception as e:
        print(f"Error getting git branch: {e}")
        sys.exit(1)
    return owner, repo, branch

def find_datasets(datasets_dir):
    """
    Recursively find all datasets in the datasets_dir.
    Returns a list of dicts with keys: source, collection, dataset, dataset_path
    """
    datasets = []
    for source in os.listdir(datasets_dir):
        source_path = os.path.join(datasets_dir, source)
        if not os.path.isdir(source_path):
            continue
        for collection in os.listdir(source_path):
            collection_path = os.path.join(source_path, collection)
            if not os.path.isdir(collection_path):
                continue
            for dataset in os.listdir(collection_path):
                dataset_path = os.path.join(collection_path, dataset)
                if not os.path.isdir(dataset_path):
                    continue
                # Must have catalog.json and collection folder
                catalog_path = os.path.join(dataset_path, 'catalog.json')
                collection_dir = os.path.join(dataset_path, collection)
                collection_json_path = os.path.join(collection_dir, 'collection.json')
                if os.path.isfile(catalog_path) and os.path.isfile(collection_json_path):
                    datasets.append({
                        'source': source,
                        'collection': collection,
                        'dataset': dataset,
                        'dataset_path': dataset_path,
                        'catalog_path': catalog_path,
                        'collection_json_path': collection_json_path
                    })
    return datasets

def parse_collection_json(collection_json_path):
    with open(collection_json_path, 'r') as f:
        data = json.load(f)
    title = data.get('title', '')
    item_assets = data.get('item_assets', {})
    assets = []
    for name, asset in item_assets.items():
        asset_type = asset.get('type', asset.get('media_type', ''))
        assets.append({'name': name, 'type': asset_type})
    return title, assets

def count_stac_items(catalog_path):
    with open(catalog_path, 'r') as f:
        data = json.load(f)
    links = data.get('links', [])
    count = sum(1 for link in links if link.get('rel') == 'item')
    return count

def make_raw_url(owner, repo, branch, rel_path):
    # rel_path should be relative to repo root
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel_path}"

def update_readme(datasets_info, readme_path, owner, repo, branch):
    # Read existing README.md
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            lines = f.readlines()
    else:
        lines = []
    # Find or create Datasets section
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        #print(f"Checking line {i}: {line.strip().lower()}")
        if line.strip().lower() == '# datasets':
            start_idx = i
            # Find where the section ends (next top-level header or EOF)
            for j in range(i+1, len(lines)):
                if lines[j].startswith('# '):
                    end_idx = j
                    break
            else:
                end_idx = len(lines)
            break
    # Build new Datasets section
    section = ['# Datasets\n', '\n']
    section.append('| Source | Collection | Dataset | Title | # Items | Assets | Catalog |\n')
    section.append('|--------|------------|---------|-------|---------|--------|---------|\n')
    for info in datasets_info:
        assets_str = ', '.join(f"{a['name']} ({a['type']})" for a in info['assets'])
        catalog_url = make_raw_url(owner, repo, branch, info['catalog_rel_path'])
        section.append(f"| {info['source']} | {info['collection']} | {info['dataset']} | {info['title']} | {info['num_items']} | {assets_str} | [catalog.json]({catalog_url}) |\n")
    section.append('\n')
    # Replace or insert section
    if start_idx is not None:
        new_lines = lines[:start_idx] + section + lines[end_idx:]
    else:
        # Append to end
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'
        new_lines = lines + section
    with open(readme_path, 'w') as f:
        f.writelines(new_lines)

def main():
    parser = argparse.ArgumentParser(description='Update README.md with dataset listing.')
    parser.add_argument('--branch', type=str, help='Override git branch name')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.resolve()
    datasets_dir = repo_root / 'datasets'
    readme_path = repo_root / 'README.md'

    owner, repo, git_branch = get_git_info()
    branch = args.branch if args.branch else git_branch

    datasets = find_datasets(str(datasets_dir))
    datasets_info = []
    for ds in datasets:
        title, assets = parse_collection_json(ds['collection_json_path'])
        num_items = count_stac_items(ds['catalog_path'])
        # catalog_rel_path: relative to repo root
        catalog_rel_path = os.path.relpath(ds['catalog_path'], repo_root)
        datasets_info.append({
            'source': ds['source'],
            'collection': ds['collection'],
            'dataset': ds['dataset'],
            'title': title,
            'assets': assets,
            'num_items': num_items,
            'catalog_rel_path': catalog_rel_path
        })
    update_readme(datasets_info, str(readme_path), owner, repo, branch)
    print(f"README.md updated with {len(datasets_info)} datasets.")

if __name__ == '__main__':
    main()
