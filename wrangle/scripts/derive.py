#!/usr/bin/env python

# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL)


import argparse
import cleaning_utils
from csv import DictReader, DictWriter
from homogenize import HOMOGENIZED_HEADERS
from loggy import loggy
from sys import stdout

LOGGY = loggy("clean")



if __name__ == '__main__':
    parser = argparse.ArgumentParser("Clean input file with specified cleaning utils")
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('cleaner', type=str)
    args = parser.parse_args()
    cleaner_name = args.cleaner
    infile = args.cleaner

    fooclean = getattr(cleaning_utils, cleaner_name)
    fooheaders = cleaning_utils.DERIVED_HEADERS[cleaner_name]
    cleaned_headers = HOMOGENIZED_HEADERS + list(fooheaders)


    # todo TK: shouldn't rely on first line of headers
    LOGGY.info('Reading from %s' % infile)
    csvin = DictReader(args.infile, fieldnames=HOMOGENIZED_HEADERS)

    csvout = DictWriter(stdout, extrasaction='ignore', fieldnames=cleaned_headers)
    csvout.writeheader()

    _headerrow = sorted(HOMOGENIZED_HEADERS)
    for row in csvin:
        if sorted(row.values()) == _headerrow:
            pass
        else:
            new_attrs = fooclean(row)
            row.update(new_attrs)
            csvout.writerow(row)
