"""
Downloads and unpacks zipped CSV files from the NYPD official data site
"""

from pathlib import Path
from shutil import unpack_archive
from sys import argv
import requests

MIN_YEAR = 2003
MAX_YEAR = 2015

FETCHED_DIR = Path('data',  'fetched', 'nypd-stop-and-frisks',)
DEST_CSV_DIR = FETCHED_DIR / 'csv'
DEST_CSV_DIR.mkdir(exist_ok=True, parents=True)
DEST_ZIP_DIR = FETCHED_DIR / 'zips'
DEST_ZIP_DIR.mkdir(exist_ok=True, parents=True)

SRC_URL_FORMAT = ("http://www.nyc.gov" +
                  "/html/nypd/downloads/zip" +
                  "/analysis_and_planning/{year}_sqf_csv.zip")

def fetch_and_save(year):
    zip_url = SRC_URL_FORMAT.format(year=year)
    print("Downloading:", zip_url)
    resp = requests.get(zip_url)
    dest_path = DEST_ZIP_DIR / '{}.zip'.format(year)
    print("Writing:", dest_path)
    dest_path.write_bytes(resp.content)

def unpack_data(year):
    dest_path = DEST_CSV_DIR
    zip_path = DEST_ZIP_DIR / '{}.zip'.format(year)
    print("Unzipping {0} into: {1}".format(zip_path, dest_path))
    unpack_archive(str(zip_path), extract_dir=str(dest_path))


if __name__ == '__main__':
    start_year = int(argv[1]) if len(argv) >= 2 else MIN_YEAR
    end_year = int(argv[2]) if len(argv) is 3 else MAX_YEAR
    print("Downloading data from:", start_year, 'to', end_year)
    print("======================")
    for year in range(start_year, end_year + 1):
        fetch_and_save(year)
        unpack_data(year)

