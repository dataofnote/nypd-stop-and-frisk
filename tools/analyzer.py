"""
Takes in a column head parameter
Reads from stdin or infile
Outputs facets in YAML
"""


import argparse
from collections import Counter
from csv import DictReader, writer
from pathlib import Path
from sys import stdout
import yaml

def facet(infile, fieldname):
    csvin = DictReader(infile)
    return Counter([row[fieldname] for row in csvin]).most_common()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Facet")
    parser.add_argument('infile', type=argparse.FileType('r'), help='file to read from')
    parser.add_argument('fieldname', type=str, help='Column name to facet by')
    args = parser.parse_args()
    infile = args.infile
    fieldname = args.fieldname

    csvout = writer(stdout)

    for k, v in facet(infile, fieldname):
        csvout.writerow([k, v])

