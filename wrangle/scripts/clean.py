"""
Standardizes values for each column according to spec.
Expects columns to have been renamed via homogenize.py
"""

from pathlib import Path

import argparse
from csv import DictReader, DictWriter
from loggy import loggy
from settings import homogenized_headers, cleaning_spec
from sys import stdout
import yaml

LOGGY = loggy('clean')
HOMOGENIZED_HEADERS = homogenized_headers()
CLEANING_SPEC = cleaning_spec()

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Clean data values according to etc/ spec")
    parser.add_argument('infile', type=argparse.FileType('r'), help='file to read from')
    args = parser.parse_args()
    infile = args.infile

    LOGGY.info("Reading from %s" % infile.name)

    # headers should not be different from HOMOGENIZED_HEADERS
    csvout = DictWriter(stdout, fieldnames=HOMOGENIZED_HEADERS)
    csvout.writeheader()

    for i, row in enumerate(DictReader(infile)):
        for header, meta in CLEANING_SPEC.items():
            cx = meta['map']
            val = row[header]
            if cx.get(val):
                LOGGY.info("{linenum}\t{header}\t{bad}\t{good}".format(linenum=i, header=header, bad=val, good=cx[val]))
                row[header] = cx[val]
        # all done with cleaning this row
        csvout.writerow(row)



# HEADERS_TO_RENAME = {


# }


# # columns relating to use of force
# USE_OF_FORCE_HEADERS = ['pf_hands', 'pf_wall', 'pf_grnd', 'pf_drwep', 'pf_ptwep', 'pf_baton', 'pf_hcuff', 'pf_pepsp', 'pf_other']

# # columns relating to whether a gun was found
# GUN_FOUND_HEADERS = ['assault_weapon', 'machine_gun', 'pistol', 'rifle']

# # guns + knives + other
# WEAPON_FOUND_HEADERS = GUN_FOUND_HEADERS + ['knifcuti', 'othrweap']

# # additional circumstances
# ADDITIONAL_CIRCUMSTANCE_HEADERS = [,]


# # columns for which answer is expected to be Y or N
# YES_OR_NO_HEADERS = ADDITIONAL_CIRCUMSTANCE_HEADERS \
#     + USE_OF_FORCE_HEADERS \
#     + WEAPON_FOUND_HEADERS + [
#         'arrest_made',
#         'contrabn',
#         'frisked',
#         'searched',
#         'sumissue',]


#     # renaming things for clarity

