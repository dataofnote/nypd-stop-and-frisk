from pathlib import Path
from sys import argv
import csv
import re

SRC_DIR = Path('data', 'fetched', 'nypd-stop-and-frisks', 'csv')
DEST_DIR = Path('data', 'normalized', 'nypd-stop-and-frisks')
DEST_DIR.mkdir(exist_ok=True, parents=True)

# headers that we copy straight on over
BOILERPLATE_HEADERS = ['race', 'age',  'sex', 'weight', 'year', 'ser_num', 'pct', 'beat', 'sector',
                        'xcoord', 'ycoord', 'addrpct', 'addrnum', 'stname', 'stinter', 'crossst',
                        'premname','arstoffn', 'sumoffen', 'crimsusp', 'detailcm',]


def foo(src_path, dest_path):
    destfile = dest_path.open('w')
    destcsv = csv.DictWriter(destfile, fieldnames=BOILERPLATE_HEADERS)
    destcsv.writeheader()
     # only 2011.csv has windows-1252 instead of ascii encoding,
    # but we open all files as windows-1252 just to be safe
    with src_path.open("r", encoding='windows-1252') as srcfile:
        for i, row in enumerate(csv.DictReader(srcfile)):
            d = {h: row[h] for h in BOILERPLATE_HEADERS}
            destcsv.writerow(d)
            if i % 10000 == 1:
                print("\t...Wrote row #", i)
    destfile.close()

if __name__ == '__main__':
    filenames = SRC_DIR.glob('*.csv')
    # optional arguments to parse just select years
    yearstrings = argv[1:] if len(argv) > 1 else []
    if yearstrings:
        print("\n\nNormalizing for the years:", yearstrings, "\n\n")
        filenames = [fn for fn in filenames if any(yr for yr in yearstrings if yr in str(fn))]

    for src_path in filenames:
        year = re.match(r'^\d{4}', src_path.name).group()
        dest_path = DEST_DIR / ('%s.csv' % year)
        print("Wrangling:", src_path)
        print('\tinto:', dest_path)
        foo(src_path, dest_path)
