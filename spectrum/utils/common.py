def validate_frequency(freq):
    return 0 < freq < 100e9

def dbm_to_watt(dbm):
    return 10 ** ((dbm - 30) / 10)
