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
    Returns a list of dicts with keys: source, collection, dataset, dataset_path, collection_path
    """
    datasets = []
    if not os.path.isdir(datasets_dir):
        return datasets

    for source in sorted(os.listdir(datasets_dir)):
        source_path = os.path.join(datasets_dir, source)
        if not os.path.isdir(source_path):
            continue
        for collection in sorted(os.listdir(source_path)):
            collection_path = os.path.join(source_path, collection)
            if not os.path.isdir(collection_path):
                continue
            # Find dataset folders (skip 'config' and hidden folders)
            for entry in sorted(os.listdir(collection_path)):
                if entry.startswith('.') or entry == 'config':
                    continue
                dataset_path = os.path.join(collection_path, entry)
                if not os.path.isdir(dataset_path):
                    continue
                catalog_path = os.path.join(dataset_path, 'catalog.json')
                # also accept catalog at dataset root (older layouts)
                if not os.path.isfile(catalog_path):
                    continue
                # If there is a dataset-level collection.json (rare), prefer it
                dataset_collection_json = os.path.join(dataset_path, 'config', 'collection.json')
                if os.path.isfile(dataset_collection_json):
                    use_collection_json = dataset_collection_json
                else:
                    # fallback to collection-level config if exists
                    coll_collection_json = os.path.join(collection_path, 'config', 'collection.json')
                    if os.path.isfile(coll_collection_json):
                        use_collection_json = coll_collection_json
                    else:
                        coll_collection_json2 = os.path.join(collection_path, 'collection.json')
                        use_collection_json = coll_collection_json2 if os.path.isfile(coll_collection_json2) else None

                datasets.append({
                    'source': source,
                    'collection': collection,
                    'dataset': entry,
                    'dataset_path': dataset_path,
                    'catalog_path': catalog_path,
                    'collection_json_path': use_collection_json,
                    'collection_path': collection_path
                })
    return datasets


def parse_collection_json(collection_json_path):
    title = ''
    assets = []
    if not collection_json_path or not os.path.isfile(collection_json_path):
        return title, assets
    try:
        with open(collection_json_path, 'r') as f:
            data = json.load(f)
        # Title may live at top-level or under properties
        title = data.get('title') or data.get('properties', {}).get('title', '') or ''
        item_assets = data.get('item_assets', {}) or data.get('assets', {})
        for name, asset in item_assets.items():
            if isinstance(asset, dict):
                asset_type = asset.get('type', asset.get('media_type', ''))
            else:
                asset_type = str(asset)
            assets.append({'name': name, 'type': asset_type})
    except Exception:
        # ignore parse issues
        pass
    return title, assets


def count_stac_items(catalog_path):
    if not catalog_path or not os.path.isfile(catalog_path):
        return 0
    try:
        with open(catalog_path, 'r') as f:
            data = json.load(f)
        links = data.get('links', [])
        if links:
            count = sum(1 for link in links if link.get('rel') == 'item')
            return count
        # Fallback: some catalogs are FeatureCollections
        features = data.get('features')
        if isinstance(features, list):
            return len(features)
    except Exception:
        pass
    return 0


def make_raw_url(owner, repo, branch, rel_path):
    # rel_path should be relative to repo root
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel_path}"


def find_collection_config_files(collection_path):
    """
    Look for the four expected config files in collection/config, allowing for common name variants.
    Returns a dict mapping label -> relative path (relative to repo root). If a file variant isn't found, returns the default expected path under config/.
    """
    config_dir = os.path.join(collection_path, 'config')
    # Map label -> list of filename candidates (checked in order)
    candidates = {
        'Collection Configuration': ['collection.json'],
        'Mosaic Config': ['mosaic_config.json', 'mosaic_configuration.json', 'mosaic-config.json'],
        'Tile Settings Config': ['tile_settings_config.json', 'tile_settings_configuration.json', 'tile-settings-config.json'],
        'Render Config': ['render_config.json', 'render_configuration.json', 'render-config.json']
    }
    found = {}
    for label, names in candidates.items():
        chosen = None
        # prefer files under config_dir
        for name in names:
            p = os.path.join(config_dir, name)
            if os.path.isfile(p):
                chosen = os.path.relpath(p, Path(__file__).parent.parent.resolve())
                break
        if chosen is None:
            # fallback to first candidate under config/ even if missing
            chosen = os.path.join('datasets', os.path.relpath(collection_path, Path(__file__).parent.parent.resolve()), 'config', names[0])
        found[label] = chosen
    return found


def update_readme(datasets_info, readme_path, owner, repo, branch):
    # Read existing README.md
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            lines = f.readlines()
    else:
        lines = []
    # Find Datasets section header (expecting '## Datasets')
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if line.strip().lower() == '## datasets' or line.strip().lower().startswith('## datasets'):
            start_idx = i
            # Find where the section ends (next '## ' header at same level) or EOF
            for j in range(i+1, len(lines)):
                if lines[j].startswith('## ') and j != i:
                    end_idx = j
                    break
            else:
                end_idx = len(lines)
            break

    repo_root = Path(__file__).parent.parent.resolve()
    # Organize datasets by source -> collection -> list[datasets]
    grouped = {}
    for info in datasets_info:
        src = info['source']
        coll = info['collection']
        grouped.setdefault(src, {})
        grouped[src].setdefault(coll, {'datasets': []})
        grouped[src][coll]['datasets'].append(info)
    # For each collection, determine config files
    for src, colls in grouped.items():
        for coll, val in colls.items():
            coll_path = val.get('datasets')[0].get('collection_path') if val.get('datasets') else None
            if coll_path:
                val['config_files'] = find_collection_config_files(coll_path)
            else:
                val['config_files'] = {}

    # Build new Datasets section (grouped with headings)
    section = ['## Datasets\n', '\n']
    for src in sorted(grouped.keys()):
        section.append(f"### {src}\n\n")
        for coll in sorted(grouped[src].keys()):
            section.append(f"#### {coll}\n\n")
            # config links
            config_files = grouped[src][coll].get('config_files', {})
            cfg_links = []
            for label in ['Collection Configuration', 'Mosaic Config', 'Tile Settings Config', 'Render Config']:
                rel = config_files.get(label)
                if not rel:
                    continue
                # ensure relative path is normalized and uses forward slashes
                rel_norm = rel.replace('\\', '/')
                url = make_raw_url(owner, repo, branch, rel_norm)
                # display short filename
                short_name = os.path.basename(rel_norm)
                cfg_links.append(f"[{short_name}]({url})")
            if cfg_links:
                section.append(' '.join(cfg_links) + '\n\n')
            # table header
            section.append('| Dataset | Title | # Items | Key Assets | Catalog |\n')
            section.append('|---------|-------|--------:|------------|--------:|\n')
            # rows
            datasets_sorted = sorted(grouped[src][coll].get('datasets', []), key=lambda x: x.get('dataset'))
            for d in datasets_sorted:
                title = d.get('title', '') or ''
                num_items = d.get('num_items', 0)
                assets_list = d.get('assets', []) or []
                key_assets = ', '.join(f"{a['name']} ({a['type']})" for a in assets_list)
                catalog_rel = os.path.relpath(d['catalog_path'], repo_root).replace('\\', '/')
                catalog_url = make_raw_url(owner, repo, branch, catalog_rel)
                section.append(f"| {d['dataset']} | {title} | {num_items} | {key_assets} | [catalog.json]({catalog_url}) |\n")
            section.append('\n')

    # Replace or insert section
    if start_idx is not None:
        new_lines = lines[:start_idx] + section + lines[end_idx:]
    else:
        # Append to end
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'
        new_lines = lines + ['\n'] + section
    with open(readme_path, 'w') as f:
        f.writelines(new_lines)


def main():
    parser = argparse.ArgumentParser(description='Update README.md with dataset listing.')
    parser.add_argument('--branch', type=str, help='Override git branch name')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.resolve()
    datasets_dir = str(repo_root / 'datasets')
    readme_path = str(repo_root / 'README.md')

    owner, repo, git_branch = get_git_info()
    branch = args.branch if args.branch else git_branch

    datasets = find_datasets(datasets_dir)
    datasets_info = []
    for ds in datasets:
        title, assets = parse_collection_json(ds.get('collection_json_path'))
        num_items = count_stac_items(ds.get('catalog_path'))
        # catalog_rel_path: relative to repo root
        catalog_rel_path = os.path.relpath(ds['catalog_path'], repo_root)
        datasets_info.append({
            'source': ds['source'],
            'collection': ds['collection'],
            'dataset': ds['dataset'],
            'title': title,
            'assets': assets,
            'num_items': num_items,
            'catalog_rel_path': catalog_rel_path,
            'catalog_path': ds['catalog_path'],
            'collection_path': ds.get('collection_path')
        })
    update_readme(datasets_info, readme_path, owner, repo, branch)
    print(f"README.md updated with {len(datasets_info)} datasets.")


if __name__ == '__main__':
    main()
