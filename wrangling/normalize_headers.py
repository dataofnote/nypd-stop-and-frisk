from pathlib import Path
from sys import argv
from project_settings import (NORMALIZED_DIR as DEST_DIR,
                              FETCHED_CSV_DIR as SRC_DIR,
                              ORIGINAL_HEADERS)
from cleaning_utils import fix_2006_format
import csv
import re


SRC_DIR = Path('data', 'fetched', 'nypd-stop-and-frisk', 'csv')
DEST_DIR = Path('data', 'normalized', 'nypd-stop-and-frisk')
DEST_DIR.mkdir(exist_ok=True, parents=True)


# returns a new row with all the ORIGINAL_HEADERS
def normalize_row(row, year_format):
    if year_format == 2006:
        row = fix_2006_format(row)

    # not all years have forceuse
    row['forceuse'] = row.get('forceuse') or ''

    nrow = {h: row[h].strip() for h in ORIGINAL_HEADERS}
    return nrow


def normalize(src_path, dest_path):
    year = int(re.search(r'\d{4}', src_path.stem).group())
    destfile = dest_path.open('w')
    destcsv = csv.DictWriter(destfile, fieldnames=ORIGINAL_HEADERS)
    destcsv.writeheader()
    # only 2011.csv has windows-1252 instead of ascii encoding,
    # but we open all files as windows-1252 just to be safe
    with src_path.open("r", encoding='windows-1252') as srcfile:
        # headers is the first line, but we lowercase the headers
        headers = srcfile.readline().strip().lower().split(',')
        records = csv.DictReader(srcfile, fieldnames=headers)
        for i, row in enumerate(records):
            nrow = normalize_row(row, year)
            destcsv.writerow(nrow)
            if i % 100000 == 99999:
                print("\t...on row #", i)
                break;

    destfile.close()





if __name__ == '__main__':
    srcfilenames = SRC_DIR.glob('*.csv')
    # optional arguments to parse just select years
    yearstrings = argv[1:] if len(argv) > 1 else []
    if yearstrings:
        # Just in case a user wants to selectively normalize a data file
        print("\n\nNormalizing for the years:", yearstrings, "\n\n")
        srcfilenames = [fn for fn in srcfilenames if any(yr for yr in yearstrings if yr in str(fn))]

    for src_path in srcfilenames:
        year = re.match(r'^\d{4}', src_path.name).group()
        dest_path = DEST_DIR / ('%s.csv' % year)
        print("Wrangling:", src_path)
        print('\tinto:', dest_path)
        normalize(src_path, dest_path)
