#!/usr/bin/env python

import argparse
import cleaning_utils
from homogenize import HOMOGENIZED_HEADERS
from csv import DictReader, DictWriter
from sys import stdout

CLEANED_HEADERS = ['datestop', 'timestop', 'datetime_stop']

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Clean input file with specified cleaning utils")
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('cleaner', type=str)
    args = parser.parse_args()
    cleaning_foo = getattr(cleaning_utils, args.cleaner)

    csvout = DictWriter(stdout, extrasaction='ignore', fieldnames=CLEANED_HEADERS)
    csvout.writeheader()

    csvin = DictReader(args.infile, fieldnames=HOMOGENIZED_HEADERS) # todo: shouldn't rely on first line of headers
    for row in csvin:
        if row == HOMOGENIZED_HEADERS:
            pass
        else:
            d = cleaning_foo(row)
            row.update(d)
            csvout.writerow(row)
