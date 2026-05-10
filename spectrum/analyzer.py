import logging
from spectrum.utils.common import validate_frequency

logging.basicConfig(level=logging.INFO)

def calculate_center_frequency(start_freq, end_freq):
    if not validate_frequency(start_freq) or not validate_frequency(end_freq):
        logging.error("Frequency out of valid range (0-100 GHz)")
        raise ValueError("Frequency out of range")
    logging.info(f"Calculating center frequency between {start_freq} and {end_freq} MHz")
    return (start_freq + end_freq) / 2

def validate_bandwidth(bandwidth):
    if bandwidth is None:
        logging.warning("bandwidth parameter is None")
        return False
    logging.debug(f"Validating bandwidth: {bandwidth} MHz")
    return bandwidth > 0