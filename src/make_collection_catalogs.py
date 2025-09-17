#!/usr/bin/env python3
"""
make_collection_catalogs.py

Create a collection-level `catalog.json` for each collection under `datasets/`.
Each generated catalog links to the dataset-level `catalog.json` files using a "child" link whose title is the dataset folder name.

Usage:
    python src/make_collection_catalogs.py [--overwrite]

This will write (or update) `datasets/{source}/{collection}/catalog.json` for each collection that has one or more dataset folders with `catalog.json`.
"""
import json
import os
import argparse
from pathlib import Path


def find_collections(datasets_root: Path):
    collections = []
    if not datasets_root.is_dir():
        return collections
    for source in sorted([p for p in datasets_root.iterdir() if p.is_dir()]):
        for collection in sorted([p for p in source.iterdir() if p.is_dir()]):
            collections.append((source.name, collection.name, collection))
    return collections


def gather_datasets_for_collection(collection_path: Path):
    datasets = []
    for entry in sorted(collection_path.iterdir()):
        if entry.name.startswith('.') or entry.name == 'config':
            continue
        if not entry.is_dir():
            continue
        catalog = entry / 'catalog.json'
        if catalog.is_file():
            datasets.append(entry.name)
    return datasets


def make_catalog_dict(source: str, collection: str, dataset_names):
    catalog = {
        "stac_version": "1.0.0",
        "type": "Catalog",
        "id": f"{source}-{collection}",
        "title": collection,
        "links": []
    }
    # self link (relative)
    catalog['links'].append({
        "rel": "self",
        "href": "catalog.json"
    })
    # child links for each dataset
    for ds in sorted(dataset_names):
        href = f"{ds}/catalog.json"
        catalog['links'].append({
            "rel": "child",
            "href": href,
            "title": ds
        })
    return catalog


def write_catalog(path: Path, catalog_dict, overwrite: bool = False):
    target = path / 'catalog.json'
    if target.exists() and not overwrite:
        print(f"Skipping existing {target} (use --overwrite to replace)")
        return False
    with open(target, 'w', encoding='utf-8') as f:
        json.dump(catalog_dict, f, indent=2, ensure_ascii=False)
    print(f"Wrote {target} with {len(catalog_dict.get('links',[]))-1} child links")
    return True


def main():
    parser = argparse.ArgumentParser(description='Create collection-level catalog.json files that link to dataset catalogs.')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing collection catalog.json files')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.resolve()
    datasets_root = repo_root / 'datasets'

    collections = find_collections(datasets_root)
    created = 0
    for source, collection, collection_path in collections:
        datasets = gather_datasets_for_collection(collection_path)
        if not datasets:
            continue
        catalog_dict = make_catalog_dict(source, collection, datasets)
        if write_catalog(collection_path, catalog_dict, overwrite=args.overwrite):
            created += 1
    print(f"Generated/updated {created} collection-level catalog.json files")

if __name__ == '__main__':
    main()
