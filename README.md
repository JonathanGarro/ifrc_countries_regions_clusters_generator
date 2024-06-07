# IFRC Countries, Regions, and Cluster Spreadsheet Generator

The [IFRC GO](go.ifrc.org) API serves a list of countries and the associated regional ID. But there isn't a simple way to connect each country to the corresponding country cluster. This simple repo offers two simple Python scripts: 

1. `get_countries_regions.py` loops through the `/country/` table in the API to download country names, NS names, and other basic geo info.
2. `match_clusters.py` connects the country from each row to the corresponding cluster. Note that you will need to transfer the output of the first script to a `.xlsx` file with two tabs: `country_data` with the output of the first script, then paste the `cluster_data.csv` data from this repo into a second worksheet called `cluster_data` in order for this second script to match.

## Instructions

1. Activate a new virtual environment with `python3 -m venv venv` and activate it with `source venv/bin/activate`
2. Install dependencies with `pip install -r requirements.txt`
3. Run `get_countries_regions.py`
4. Open the outputted CSV and save as `.xlsx`
5. Paste the `cluster_data.csv` data as a new worksheet in that `.xlsx` file. Name the two worksheets `country_data` and `cluster_data`.
6. Run `match_clusters.py` 