s# MPC Pro Datasets
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
| planetary_computer | naip | los_angeles | NAIP: National Agriculture Imagery Program | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/los_angeles/catalog.json) |
| planetary_computer | naip | denver | NAIP: National Agriculture Imagery Program | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/denver/catalog.json) |
| planetary_computer | naip | phoenix | NAIP: National Agriculture Imagery Program | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/phoenix/catalog.json) |
| planetary_computer | naip | seattle | NAIP: National Agriculture Imagery Program | 25 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/seattle/catalog.json) |
| planetary_computer | naip | mount_rainier | NAIP: National Agriculture Imagery Program | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/mount_rainier/catalog.json) |
| planetary_computer | naip | washington_dc | NAIP: National Agriculture Imagery Program | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/washington_dc/catalog.json) |
| planetary_computer | naip | statue_of_liberty | NAIP: National Agriculture Imagery Program | 10 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/statue_of_liberty/catalog.json) |
| planetary_computer | naip | glacier | NAIP: National Agriculture Imagery Program | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/glacier/catalog.json) |
| planetary_computer | naip | miami | NAIP: National Agriculture Imagery Program | 17 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/miami/catalog.json) |
| planetary_computer | naip | houston | NAIP: National Agriculture Imagery Program | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/houston/catalog.json) |
| planetary_computer | naip | manhattan | NAIP: National Agriculture Imagery Program | 15 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/manhattan/catalog.json) |
| planetary_computer | naip | mount_rushmore | NAIP: National Agriculture Imagery Program | 15 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/mount_rushmore/catalog.json) |
| planetary_computer | naip | san_francisco | NAIP: National Agriculture Imagery Program | 18 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/san_francisco/catalog.json) |
| planetary_computer | naip | everglades | NAIP: National Agriculture Imagery Program | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/everglades/catalog.json) |
| planetary_computer | naip | yellowstone | NAIP: National Agriculture Imagery Program | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/yellowstone/catalog.json) |
| planetary_computer | naip | great_smoky_mountains | NAIP: National Agriculture Imagery Program | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/great_smoky_mountains/catalog.json) |
| planetary_computer | naip | grand_canyon | NAIP: National Agriculture Imagery Program | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/grand_canyon/catalog.json) |
| planetary_computer | naip | chicago | NAIP: National Agriculture Imagery Program | 35 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/chicago/catalog.json) |
| planetary_computer | naip | arches | NAIP: National Agriculture Imagery Program | 25 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/arches/catalog.json) |
| planetary_computer | naip | yosemite | NAIP: National Agriculture Imagery Program | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/yosemite/catalog.json) |

