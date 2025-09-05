# MPC Pro Sample Datasets
A collection of sample geospatial datasets curated for quick evaluation and testing of the MPC Pro Bulk Ingestion API (and UI). 

## Organization
The `datasets/` folder contains structured sample subsets grouped first by the original data source (e.g. `planetary_computer`) and then by a STAC collection identifier (e.g. `naip`). Each dataset folder under a collection represents a themed geographic subset (city, park, landmark, etc.). The folder structure beneath `datasets/` looks like this:

```
datasets/
├── {source}/
│   ├── {collection}
|   |   |── config/
            ├──collection.json
            ├──mosaic_config.json
            ├──tile_settings_config.json
            ├──render_config.json
│   │   ├── {dataset}/
            ├──{stac-item-folder-1}/
            ├──{stac-item-folder-2}/
            ├──catalog.json
```
Where:
* `{source}` – Origin/source grouping (e.g. `planetary_computer`).
* `{collection}` – STAC collection identifier (e.g. `naip`).
* `{dataset}` – Individual sample subset (e.g. `manhattan`).
* `{stac-item-folder}` – One or more STAC Item directories with item JSON + assets.
* `catalog.json` – Root catalog for that subset linking to its items.
* `collection.json` – A baseline MPC Pro [STAC collection specification](https://learn.microsoft.com/azure/planetary-computer/create-collection-web-interface).
* `mosaic_config.json` - A baseline collection [mosaic configuration](https://learn.microsoft.com/azure/planetary-computer/mosaic-configurations-for-collections)
* `tile_settings_config.json` - A baseline collection [tile settings configuration](https://learn.microsoft.com/azure/planetary-computer/tile-settings)
* `render_config.json` - A baseline collection [render configuration](https://learn.microsoft.com/en-us/azure/planetary-computer/render-configuration)

## Usage
You can ingest these datasets into MPC Pro via the Bulk Ingestion API or the [Bulk Ingestion UI](https://learn.microsoft.com/azure/planetary-computer/ingest-via-web-interface).

High‑level ingestion steps:
1. Create (or confirm) the STAC collection in MPC Pro using the provided collection definition (see links below).
2. Start a Bulk Ingestion run pointing at the raw GitHub URL of a dataset's `catalog.json`.
3. (Optional) Apply mosaic definitions, render options, and tile settings for richer visualization.

## Datasets

### Planetary Computer
Each of these collections and datasets originate from [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/).

#### NAIP (National Agriculture Imagery Program)

**Collection Configuration**: [Collection JSON](/datasets/planetary_computer/naip/config/naip_collection.json) · [Mosaic Config](/datasets/planetary_computer/naip/config/naip_mosaic_configuration.json) · [Tile Settings Config]() · [Render Config](/datasets/planetary_computer/naip/config/render_config.json)

| Dataset | Title | # Items | Key Assets | Catalog |
|---------|-------|---------|------------|---------|
| los_angeles | NAIP: National Agriculture Imagery Program | 40 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/los_angeles/catalog.json) |
| denver | NAIP: National Agriculture Imagery Program | 30 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/denver/catalog.json) |
| phoenix | NAIP: National Agriculture Imagery Program | 30 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/phoenix/catalog.json) |
| seattle | NAIP: National Agriculture Imagery Program | 25 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/seattle/catalog.json) |
| mount_rainier | NAIP: National Agriculture Imagery Program | 30 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/mount_rainier/catalog.json) |
| washington_dc | NAIP: National Agriculture Imagery Program | 30 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/washington_dc/catalog.json) |
| statue_of_liberty | NAIP: National Agriculture Imagery Program | 10 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/statue_of_liberty/catalog.json) |
| glacier | NAIP: National Agriculture Imagery Program | 50 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/glacier/catalog.json) |
| miami | NAIP: National Agriculture Imagery Program | 17 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/miami/catalog.json) |
| houston | NAIP: National Agriculture Imagery Program | 40 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/houston/catalog.json) |
| manhattan | NAIP: National Agriculture Imagery Program | 15 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/manhattan/catalog.json) |
| mount_rushmore | NAIP: National Agriculture Imagery Program | 15 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/mount_rushmore/catalog.json) |
| san_francisco | NAIP: National Agriculture Imagery Program | 18 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/san_francisco/catalog.json) |
| everglades | NAIP: National Agriculture Imagery Program | 40 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/everglades/catalog.json) |
| yellowstone | NAIP: National Agriculture Imagery Program | 50 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/yellowstone/catalog.json) |
| great_smoky_mountains | NAIP: National Agriculture Imagery Program | 40 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/great_smoky_mountains/catalog.json) |
| grand_canyon | NAIP: National Agriculture Imagery Program | 50 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/grand_canyon/catalog.json) |
| chicago | NAIP: National Agriculture Imagery Program | 35 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/chicago/catalog.json) |
| arches | NAIP: National Agriculture Imagery Program | 25 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/arches/catalog.json) |
| yosemite | NAIP: National Agriculture Imagery Program | 50 | image (COG), metadata, thumbnail | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-naip-datasets/datasets/planetary_computer/naip/yosemite/catalog.json) |

