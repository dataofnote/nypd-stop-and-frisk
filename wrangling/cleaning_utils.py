from copy import copy
USE_OF_FORCE_HEADERS = ['pf_hands', 'pf_wall', 'pf_grnd', 'pf_drwep', 'pf_ptwep', 'pf_baton', 'pf_hcuff', 'pf_pepsp', 'pf_other']


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










def derive_was_force_used(row):
    """
    Returns 'Y' if any of the row's values for force-related attributes is 'Y';
    otherwise, returns 'N'
    """
    return next((row[c] for c in USE_OF_FORCE_HEADERS if row[c] == 'Y'), 'N')

def derive_datetime_stop(datestop, timestop):
    if len(timestop) >= 3:
        # 318 => (03:18)
        # 15:12 => (15:12)
        clean_timestop = "{hrs}:{min}".format(hrs=timestop[0:2].rjust(2, '0'),
                                              min=timestop[2:].rjust(2, '0'))
    else:
        # 5  => (00:05)
        # 14 => (00:14)
        # just pad the string and prepend 00 as the hours value
        clean_timestop = "{hrs}:{min}".format(hrs='00',
                                              min=timestop.rjust(2, '0'))

    # Fix date
    # 7042014 => 2014-07-04
    # 12012011 => 2011-12-01
    datestop = datestop.rjust(8, '0')
    cleaned_datestop = '{yr}-{mth}-{day} {time}'.format(yr=datestop[-4:], mth=datestop[0:2],
                                                        day=datestop[2:4], time=timestop)
    return cleaned_datestop
