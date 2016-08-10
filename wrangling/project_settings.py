from pathlib import Path

FETCHED_DIR = Path('data',  'fetched', 'nypd-stop-and-frisk',)
FETCHED_CSV_DIR = FETCHED_DIR / 'csv'
FETCHED_CSV_DIR.mkdir(exist_ok=True, parents=True)
FETCHED_ZIP_DIR = FETCHED_DIR / 'zips'
FETCHED_ZIP_DIR.mkdir(exist_ok=True, parents=True)
NORMALIZED_DIR = Path('data',  'normalized', 'nypd-stop-and-frisk',)
NORMALIZED_DIR.mkdir(exist_ok=True, parents=True)


ORIGINAL_HEADERS = ["year","pct","ser_num","datestop","timestop","recstat","inout",
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
