#!/usr/bin/env bash
#
# Pass in 1 argument: number representing year of file to download
# stdout: unzipped text
if [ $# -ne 1 ]; then
    (>&2 echo "ERROR: Expecting exactly one argument: year, e.g. 2012")
    exit 2
fi

#
# Note: Downloaded zip file is expected to have a single file,
# e.g.
# http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2015_sqf_csv.zip
# Should contain only:
# 2015_sqf_csv.csv
# A warning is thrown otherwise


SRC_URL_DOMAIN='http://www.nyc.gov'
SRC_URL_PATH='/html/nypd/downloads/zip/analysis_and_planning'
SRC_URL_STEM='sqf_csv.zip'

zipurl=${SRC_URL_DOMAIN}${SRC_URL_PATH}/${1}_${SRC_URL_STEM}
zipdest=$(mktemp)
(>&2 echo "INFO: Downloading $zipurl")
(>&2 echo "INFO: Saving (temporarily) to $zipdest")
curl "$zipurl" -o "$zipdest"
# count files
# filecount=$(unzip -l $zipdest | tail -n 1 | awk '{ print $2 }')
# if [[]]
(>&2 unzip -l "$zipdest")

filecount=$(unzip -l "$zipdest" | tail -n 1 | awk '{ print $2 }')
if [[ "$filecount" -ne 1 ]]; then
    echo "Warning: Expecting zipfile to contain 1 file, not $filecount"
fi

unzip -q -p "$zipdest"

