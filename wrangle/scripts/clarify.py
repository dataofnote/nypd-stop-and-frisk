HEADERS_TO_RENAME = {
    'ac_assoc': 'ac_assocation_with_criminals',
    'ac_cgdir': 'ac_changeed_direction',
    'ac_evasv': 'ac_evasive_to_questions',
    'ac_incid': 'ac_high_crime_area',
    'ac_inves': 'ac_ongoing_investigation',
    'ac_proxm': 'ac_proximity_to_scene',
    'ac_rept':  'ac_reported_by_person',
    'ac_stsnd': 'ac_sights_sounds',
    'ac_time':  'ac_time_of_day',

    'arstmade': 'arrest_made',
    'asltweap': 'assault_weapon',

    'linecm': 'additional_details'
    'machgun': 'machine_gun',

    'officrid' : 'officer_id_card',
    'offshld' : 'officer_shield',
    'offunif' : 'officer_uniformed',
    'offverb' : 'officer_verbal_statement',
    'othfeatr' : 'suspect_other_features',
    'othpers' : 'other_persons_stopped',
    'perobs': 'period_of_observation',
    'perstop': 'period_of_stop',
    'pf_drwep': 'pf_weapon_drawn',
    'pf_grnd': 'pf_suspect_on_ground',
    'pf_hcuff': 'pf_handcuffed',
    'pf_ptwep': 'pf_weapon_pointed',
    'pf_wall': 'pf_suspect_against_wall',

    'post':   'loc_post',
    'premname': 'loc_premise_name',
    'premtype': 'loc_premise_type',

    'recstat': 'record_status',
    'repcmd' : 'reporting_officer_command',
    'rescode' : 'resident_code_location',
    'revcmd'  : 'reviewing_officer_command',
    'rf_attir': 'rf_out_of_season_attire',
    'rf_bulg': 'rf_suspicious_bulge',
    'rf_furt': 'rf_furtive_movements',
    'rf_knowl': 'rf_prior_knowledge_of_criminal_behavior',
    'rf_othsw': 'rf_other_suspicion_of_weapons',
    'rf_rfcmp': 'rf_refused_to_comply',
    'rf_vcrim': 'rf_violent_crime_suspected',
    'rf_verbl': 'rf_verbal_threats',

    'riflshot': 'rifle',

    'sb_admis': 'sb_admission_by_suspect',
    'sb_hdobj': 'sb_hard_object',
    'sb_other': 'sb_other',
    'sb_outln': 'sb_outline_of_weapon',

    'ser_num': 'ucb_serialnum',
    'stinter':
    'stname':
    'sumissue':
    'sumoffen':

    'trhsloc': 'location_housing_or_transit_authority',


}


# columns relating to use of force
USE_OF_FORCE_HEADERS = ['pf_hands', 'pf_wall', 'pf_grnd', 'pf_drwep', 'pf_ptwep', 'pf_baton', 'pf_hcuff', 'pf_pepsp', 'pf_other']

# columns relating to whether a gun was found
GUN_FOUND_HEADERS = ['assault_weapon', 'machine_gun', 'pistol', 'rifle']

# guns + knives + other
WEAPON_FOUND_HEADERS = GUN_FOUND_HEADERS + ['knifcuti', 'othrweap']

# additional circumstances
ADDITIONAL_CIRCUMSTANCE_HEADERS = [,]


# columns for which answer is expected to be Y or N
YES_OR_NO_HEADERS = ADDITIONAL_CIRCUMSTANCE_HEADERS \
    + USE_OF_FORCE_HEADERS \
    + WEAPON_FOUND_HEADERS + [
        'arrest_made',
        'contrabn',
        'frisked',
        'searched',
        'sumissue',]


    # renaming things for clarity

