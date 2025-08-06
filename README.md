# MPC Pro Datasets
A collection of sample Datasets that can be easily imported into MPC Pro with the Bulk Ingestion API. 

## Organization
The 'datasets' folder in this repository contains a colleciton of geospatial datasets that can be used to test the MPC Pro Bulk Ingestion API. The folder structure beneath 'datasets' looks like this:

```
datasets/
├── {source}/
│   ├── {collection}
│   │   ├── {dataset}/
            ├──{collection-folder}/
                ├──colleciton.json
            ├──{stac-item-folder-1}/
            ├──{stac-item-folder-2}/
            ├──catalog.json
```
Where:
- `{source}` is the name of the source of the dataset (e.g. 'planetary_computer')
- `{collection}` is the name of the collection that the dataset belongs to (e.g. 'naip')
- `{dataset}` is the name of the dataset (e.g. 'manhattan')
- `{collection-folder}` is the folder that contains the collection.json file for the dataset
- `{stac-item-folder}` is the folder that contains the STAC item files for the dataset
- `collection.json` is the file that contains the collection metadata for the dataset
- `catalog.json` is the file that contains the catalog metadata for the dataset

## Usage
To use these datasets, you can import them into MPC Pro using the Bulk Ingestion API or the [Bulk Ingestion UI](https://learn.microsoft.com/azure/planetary-computer/ingest-via-web-interface).

Follow these high-level steps to import a dataset:
1. Use either the Web UI or the STAC API to create a new collection in MPC Pro.
    * Use the `collection.json` file in the `{collection-folder}` as the tempalte to create the collection.
2. Provide the URL of the catalog.json fro the dataset to the Bulk Ingestion API or the Web UI.
3. (TO DO) Update colleciton mosaic, tile, and render configurations as needed.

# Datasets

| Source | Collection | Dataset | Title | # Items | Assets | Catalog |
|--------|------------|---------|-------|---------|--------|---------|
| planetary_computer | naip | manhattan | NAIP: National Agriculture Imagery Program | 15 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/initial-naip-datasets/datasets/planetary_computer/naip/manhattan/catalog.json) |

