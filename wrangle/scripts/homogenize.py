#!/usr/bin/env python
"""
Makes sure all files follow the same schema, including older years
that don't have the columns from newer years (values are left blank)

Headers are renamed according to etc/headers_renamed.csv
"""

import argparse
from copy import copy
from csv import DictReader, DictWriter
from loggy import loggy
from settings import homogenized_headers, normalized_headers, renamed_headers_map
import re
from sys import stdout

LOGGY = loggy('homogenize')

HOMOGENIZED_HEADERS = homogenized_headers()
NORMALIZED_HEADERS = normalized_headers()
RENAMED_HEADERS_MAP = renamed_headers_map()



def fix_2006_format(row):
    nrow = copy(row)
    nrow['addrpct'] = row['adrpct']
    nrow['addrnum'] = row['adrnum']
    nrow['premname'] = row['prenam']
    nrow['premtype'] = row['premtyp']
    nrow['rescode'] = row['rescod']
    nrow['stname'] = row['strname']
    nrow['stinter'] = row['strintr']
    nrow['detailcm'] = row['details_']
    nrow['dettypcm'] = row['dettyp_c']
    nrow['linecm'] = "" # is there really no linecm?
    return nrow


def homogenize_row(row, year_format):
    nrow = normalize_row(row, year_format)
    rename_headers(nrow)
    return nrow


def normalize_row(row, year_format):
    """
    Returns a dict with values or blanks for all keys in NORMALIZED_HEADERS
    Whitespace is stripped
    """
    if year_format == 2006:
        row = fix_2006_format(row)
    # not all years have forceuse
    row['forceuse'] = row.get('forceuse') or ''
    return {h: row[h].strip() for h in NORMALIZED_HEADERS}

def rename_headers(row):
    """returns nothing, alters row"""
    for header, alias in RENAMED_HEADERS_MAP.items():
        row[alias] = row[header]

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Homogenize data format and headers for clarity")
    parser.add_argument('infile', type=argparse.FileType('r', encoding='windows-1252'), help='file to read from')
    parser.add_argument('year', type=int, help='Explicitly state the year of the file')
    args = parser.parse_args()
    infile = args.infile
    year = args.year

    LOGGY.info("Reading from %s" % infile.name)
    LOGGY.info("Formatting it based on specs for %s" % year)

    # read in first line, convert to lower-case headers for less headaches
    inputheaders = infile.readline().strip().lower().split(',')
    csvin = DictReader(infile, fieldnames=inputheaders)

    csvout = DictWriter(stdout, fieldnames=HOMOGENIZED_HEADERS, extrasaction='ignore')
    csvout.writeheader()

    for r in csvin:
        row = homogenize_row(r, year_format=year)
        csvout.writerow(row)
