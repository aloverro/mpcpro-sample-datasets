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

### maxar

#### open-data-program

[catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/catalog.json) [collection.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/config/collection.json) [mosaic_configuration.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/config/mosaic_configuration.json) [tile_settings_configuration.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/config/tile_settings_configuration.json) [render_configuration.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/config/render_configuration.json)

| Dataset | Title | # Items | Key Assets | Catalog |
|---------|-------|--------:|------------|--------:|
| India-Floods-Oct-2023 | Maxar Open Data Program | 51 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/India-Floods-Oct-2023/catalog.json) |
| Kalehe-DRC-Flooding-5-8-23 | Maxar Open Data Program | 24 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/Kalehe-DRC-Flooding-5-8-23/catalog.json) |
| Maui-Hawaii-fires-Aug-23 | Maxar Open Data Program | 123 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/Maui-Hawaii-fires-Aug-23/catalog.json) |
| NWT-Canada-Aug-23 | Maxar Open Data Program | 86 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/NWT-Canada-Aug-23/catalog.json) |
| New-Zealand-Flooding23 | Maxar Open Data Program | 37 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/New-Zealand-Flooding23/catalog.json) |
| Nigeria-Floods-Sept-2024 | Maxar Open Data Program | 18 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/Nigeria-Floods-Sept-2024/catalog.json) |
| covid19-sierra-leone | Maxar Open Data Program | 32 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/covid19-sierra-leone/catalog.json) |
| shovi-georgia-landslide-8Aug23 | Maxar Open Data Program | 25 | visual (image/tiff; application=geotiff) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/maxar/open-data-program/shovi-georgia-landslide-8Aug23/catalog.json) |

### planetary_computer

#### naip

[catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/catalog.json) [collection.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/config/collection.json) [mosaic_config.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/config/mosaic_config.json) [tile_settings_config.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/config/tile_settings_config.json) [render_config.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/config/render_config.json)

| Dataset | Title | # Items | Key Assets | Catalog |
|---------|-------|--------:|------------|--------:|
| arches | NAIP (MPC Pro Sample Datasets) | 25 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/arches/catalog.json) |
| atl | NAIP (MPC Pro Sample Datasets) | 46 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/atl/catalog.json) |
| chicago | NAIP (MPC Pro Sample Datasets) | 35 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/chicago/catalog.json) |
| clt | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/clt/catalog.json) |
| den | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/den/catalog.json) |
| denver | NAIP (MPC Pro Sample Datasets) | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/denver/catalog.json) |
| dfw | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/dfw/catalog.json) |
| everglades | NAIP (MPC Pro Sample Datasets) | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/everglades/catalog.json) |
| glacier | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/glacier/catalog.json) |
| grand_canyon | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/grand_canyon/catalog.json) |
| great_smoky_mountains | NAIP (MPC Pro Sample Datasets) | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/great_smoky_mountains/catalog.json) |
| houston | NAIP (MPC Pro Sample Datasets) | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/houston/catalog.json) |
| las | NAIP (MPC Pro Sample Datasets) | 36 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/las/catalog.json) |
| lax | NAIP (MPC Pro Sample Datasets) | 36 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/lax/catalog.json) |
| los_angeles | NAIP (MPC Pro Sample Datasets) | 40 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/los_angeles/catalog.json) |
| manhattan | NAIP (MPC Pro Sample Datasets) | 15 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/manhattan/catalog.json) |
| mco | NAIP (MPC Pro Sample Datasets) | 42 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/mco/catalog.json) |
| miami | NAIP (MPC Pro Sample Datasets) | 17 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/miami/catalog.json) |
| mount_rainier | NAIP (MPC Pro Sample Datasets) | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/mount_rainier/catalog.json) |
| mount_rushmore | NAIP (MPC Pro Sample Datasets) | 15 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/mount_rushmore/catalog.json) |
| ord | NAIP (MPC Pro Sample Datasets) | 48 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/ord/catalog.json) |
| phoenix | NAIP (MPC Pro Sample Datasets) | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/phoenix/catalog.json) |
| phx | NAIP (MPC Pro Sample Datasets) | 28 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/phx/catalog.json) |
| san_francisco | NAIP (MPC Pro Sample Datasets) | 18 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/san_francisco/catalog.json) |
| sea | NAIP (MPC Pro Sample Datasets) | 24 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/sea/catalog.json) |
| seattle | NAIP (MPC Pro Sample Datasets) | 25 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/seattle/catalog.json) |
| statue_of_liberty | NAIP (MPC Pro Sample Datasets) | 10 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/statue_of_liberty/catalog.json) |
| washington_dc | NAIP (MPC Pro Sample Datasets) | 30 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/washington_dc/catalog.json) |
| yellowstone | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/yellowstone/catalog.json) |
| yosemite | NAIP (MPC Pro Sample Datasets) | 50 | image (image/tiff; application=geotiff; profile=cloud-optimized), metadata (text/plain), thumbnail (image/jpeg) | [catalog.json](https://raw.githubusercontent.com/aloverro/mpcpro-sample-datasets/expand-maxar-datasets/datasets/planetary_computer/naip/yosemite/catalog.json) |

