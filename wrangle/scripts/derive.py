#!/usr/bin/env python

# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL)


import argparse
from csv import DictReader, DictWriter
import derivation_utils
from derivation_utils import DERIVED_HEADERS
from homogenize import HOMOGENIZED_HEADERS
from loggy import loggy
from sys import stdout

LOGGY = loggy("clean")



if __name__ == '__main__':
    parser = argparse.ArgumentParser("Clean input file with specified cleaning utils")
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('derivations', type=str, nargs='*')
    args = parser.parse_args()
    infile = args.infile
    derivation_names = args.derivations
    LOGGY.info('Running derivations: %s' % derivation_names)

    LOGGY.info('Reading from %s' % infile)
    csvin = DictReader(args.infile)

    out_headers = HOMOGENIZED_HEADERS + DERIVED_HEADERS
    csvout = DictWriter(stdout, extrasaction='ignore', fieldnames=out_headers)
    csvout.writeheader()

    derivers = [getattr(derivation_utils, dn) for dn in derivation_names]
    for row in csvin:
        for derivefoo in derivers:
            new_attrs, warnings = derivefoo(row)
            if warnings:
                LOGGY.warn(warnings)
            row.update(new_attrs)
        csvout.writerow(row)
