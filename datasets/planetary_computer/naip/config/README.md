# NAIP Configuration (Relocated)

This directory now hosts sample configuration JSON files for the NAIP collection:

- `naip_collection.json` – Collection definition used to create the collection in a GeoCatalog.
- `naip_mosaic_configuration.json` – Example mosaic and render option definitions.
- `naip_tile_settings.json` – Tile and rendering defaults.

These were moved from the previous top-level `config/` directory to live directly under the NAIP dataset tree:
`datasets/planetary_computer/naip/config/`.

Update any tooling or deployment scripts that referenced the old path.
