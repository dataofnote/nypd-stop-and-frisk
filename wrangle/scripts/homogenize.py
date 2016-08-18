#!/usr/bin/env python

from copy import copy
from csv import DictReader, DictWriter
from sys import argv, stdout
import re




HOMOGENIZED_HEADERS = ["year","pct","ser_num","datestop","timestop","recstat","inout",
                "trhsloc","perobs","crimsusp","perstop","typeofid","explnstp","othpers",
                "arstmade","arstoffn","sumissue","sumoffen","compyear","comppct","offunif",
                "officrid","frisked","searched","contrabn","adtlrept","pistol","riflshot",
                "asltweap","knifcuti","machgun","othrweap","pf_hands","pf_wall","pf_grnd",
                "pf_drwep","pf_ptwep","pf_baton","pf_hcuff","pf_pepsp","pf_other","radio",
                "ac_rept","ac_inves","rf_vcrim","rf_othsw","ac_proxm","rf_attir","cs_objcs",
                "cs_descr","cs_casng","cs_lkout","rf_vcact","cs_cloth","cs_drgtr","ac_evasv",
                "ac_assoc","cs_furtv","rf_rfcmp","ac_cgdir","rf_verbl","cs_vcrim","cs_bulge",
                "cs_other","ac_incid","ac_time","rf_knowl","ac_stsnd","ac_other","sb_hdobj",
                "sb_outln","sb_admis","sb_other","repcmd","revcmd","rf_furt","rf_bulg",
                "offverb","offshld","forceuse","sex","race","dob","age","ht_feet","ht_inch",
                "weight","haircolr","eyecolor","build","othfeatr","addrtyp","rescode","premtype",
                "premname","addrnum","stname","stinter","crossst","aptnum","city","state","zip",
                "addrpct","sector","beat","post","xcoord","ycoord","dettypcm","linecm","detailcm",
            ]


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

def homogonize_row(row, year_format):
    if year_format == 2006:
        row = fix_2006_format(row)
    # not all years have forceuse
    row['forceuse'] = row.get('forceuse') or ''
    return {h: row[h].strip() for h in HOMOGENIZED_HEADERS}




if __name__ == '__main__':
    if len(argv) != 2:
        raise IOError("Expects exactly one argument: name of file to be parsed.")

    src_path = argv[1]
    year = int(re.search(r'\d{4}(?=\.csv)', src_path).group())
    with open(src_path, "r", encoding='windows-1252') as src_file:
        # read in first line, convert to lower-case headers for less headaches
        inputheaders = src_file.readline().strip().lower().split(',')

        csvout = DictWriter(stdout, fieldnames=HOMOGENIZED_HEADERS)
        csvout.writeheader()
        for row in DictReader(src_file, fieldnames=inputheaders):
            hrow = homogonize_row(row, year_format=year)
            csvout.writerow(hrow)
