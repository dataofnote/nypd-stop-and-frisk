from csv import reader
from pathlib import Path

ETC_PATH = Path('wrangle', 'scripts', 'etc')
HOMOGENIZED_HEADERS_PATH = ETC_PATH /'headers_homogenized.csv'
RENAMED_HEADERS_PATH = ETC_PATH / 'headers_renamed.csv'


def homogenized_headers():
    return [s.strip() for s in HOMOGENIZED_HEADERS_PATH.read_text().splitlines()]

def renamed_headers_map():
    headers = list(reader(RENAMED_HEADERS_PATH.read_text().splitlines()))
    return dict(headers)
