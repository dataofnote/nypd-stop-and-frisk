from csv import reader
from pathlib import Path
import yaml

ETC_PATH = Path('wrangle', 'scripts', 'etc')
HOMOGENIZED_HEADERS_PATH = ETC_PATH /'headers_homogenized.txt'
NORMALIZED_HEADERS_PATH = ETC_PATH /'headers_normalized.txt'
RENAMED_HEADERS_PATH = ETC_PATH / 'headers_renamed.csv'
DERIVED_HEADERS_PATH = ETC_PATH / 'headers_derived.txt'
YESNO_COLUMNS_PATH = ETC_PATH / 'yesno_columns.txt'
FORCE_USED_HEADERS_PATH = ETC_PATH / 'headers_force_used.txt'


# def cleaning_spec():
#     return yaml.load(Path('wrangle', 'scripts', 'etc', 'values_cleaned.yaml').read_text())

def homogenized_headers():
    return [s.strip() for s in HOMOGENIZED_HEADERS_PATH.read_text().splitlines()]


def normalized_headers():
    return [s.strip() for s in NORMALIZED_HEADERS_PATH.read_text().splitlines()]

def renamed_headers_map():
    headers = list(reader(RENAMED_HEADERS_PATH.read_text().splitlines()))
    return dict(headers)


def derived_headers():
    return [s.strip() for s in DERIVED_HEADERS_PATH.read_text().splitlines()]



def yesno_columns():
    return [s.strip() for s in YESNO_COLUMNS_PATH.read_text().splitlines()]

def force_used_headers():
    """
    these headers are ranked in order from most serious/rarest (e.g. weapon_pointed) to least (e.g. other, hands)
    """
    return [s.strip() for s in FORCE_USED_HEADERS_PATH.read_text().splitlines()]
