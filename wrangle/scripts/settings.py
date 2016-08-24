from csv import reader
from pathlib import Path
import yaml

ETC_PATH = Path('wrangle', 'scripts', 'etc')
HOMOGENIZED_HEADERS_PATH = ETC_PATH /'headers_homogenized.txt'
NORMALIZED_HEADERS_PATH = ETC_PATH /'headers_normalized.txt'
RENAMED_HEADERS_PATH = ETC_PATH / 'headers_renamed.csv'


def cleaning_spec():
    return yaml.load(Path('wrangle', 'scripts', 'etc', 'values_cleaned.yaml').read_text())

def homogenized_headers():
    return [s.strip() for s in HOMOGENIZED_HEADERS_PATH.read_text().splitlines()]


def normalized_headers():
    return [s.strip() for s in NORMALIZED_HEADERS_PATH.read_text().splitlines()]

def renamed_headers_map():
    headers = list(reader(RENAMED_HEADERS_PATH.read_text().splitlines()))
    return dict(headers)
