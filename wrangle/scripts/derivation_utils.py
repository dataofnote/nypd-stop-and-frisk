from pathlib import Path
from settings import derived_headers, yesno_columns, force_used_headers
import pyproj
NYSP1983_PROJ = pyproj.Proj(init="ESRI:102718", preserve_units=True)


# these represent new column headers that are created
# DERIVED_HEADERS = {
#     'derive_datetime_stop': ('datetime_stop',),
#     'derive_use_of_force': ('force_used',),
#     'derive_latlng': ('longitude', 'latitude',),
#     'derive_yesno': (),
# }


FORCE_USED_HEADERS = force_used_headers()
DERIVED_HEADERS = derived_headers()
YESNO_COLUMNS = yesno_columns()

def derive_datetime_stop(datarow):
    """
    Attempts to complete incomplete datetime strings
    `datarow` is a dict, presumably a data row from homogenized
    stop-n-frisk data with `datestop` and `timestop` columns

    Returns: a dict:
        {'datetime_stop': '2014-07-04 03:18'}

    with a string representing the datetime in ISO format

    e.g.
    7042014,318 => 2014-07-04 03:18
    """

    datestop = datarow['datestop']
    timestop = datarow['timestop']

    if len(timestop) >= 3:
        # 318 => (03:18)
        # 15:12 => (15:12)
        cleaned_time = "{hrs}:{min}".format(hrs=timestop[0:2].rjust(2, '0'),
                                              min=timestop[2:].rjust(2, '0'))
    else:
        # 5  => (00:05)
        # 14 => (00:14)
        # just pad the string and prepend 00 as the hours value
        cleaned_time = "{hrs}:{min}".format(hrs='00', min=timestop.rjust(2, '0'))
    # Fix date
    # 7042014 => 2014-07-04
    # 12012011 => 2011-12-01
    dx = datestop.rjust(8, '0')
    cleaned_date = '{yr}-{mth}-{day}'.format(yr=dx[-4:], mth=dx[0:2], day=dx[2:4])

    return {'datetime_stop': "{0} {1}".format(cleaned_date, cleaned_time)}



def derive_force_type_used(row):
    """
    The FORCE_USED_HEADERS is a list in descending order of serious, starting
    with "pf_weapon_pointed" to "pf_hands"

    This function returns the most serious/rarest type of force, e.g. "weapon_pointed"
    that has a 'Y' in the column. Else None is returned

    Note: probably should run derive_yesno to normalize this to Y or N...
    """
    forcetype = next((c.split('_', 1)[1] for c in FORCE_USED_HEADERS if row[c] == 'Y'), None)
    return {'force_type_used': forcetype}


def derive_latlng(row):
    if row['xcoord'] and row['ycoord']:
        lnglat = NYSP1983_PROJ(int(row['xcoord']),
                               int(row['ycoord']),
                               inverse=True)
        return dict(zip(['longitude', 'latitude'], [round(c, 5) for c in lnglat]))
    else:
        return {'longitude': None, 'latitude': None}

def derive_yesno(row):
    """helper method to normalize Y/N/'' columns
    `val`: str; expected to be y,n,(None),Y,N
    Returns: str; 'Y' or 'N'; blanks are removed
    """
    d = {}
    for h in YESNO_COLUMNS:
        val = row[h].upper()
        if val in ['Y', '1']:
            d[h] = 'Y'
        elif val in ['N', '0']:
            d[h] = 'N'
        elif not val:
            d[h] = ""
        else:
            raise ValueError("Column %s had an unexpected value of %s" % (h, row[h]))
    return d

