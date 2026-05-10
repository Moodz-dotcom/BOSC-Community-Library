import logging

logging.basicConfig(level=logging.INFO)

def calculate_center_frequency(start_freq, end_freq):
    logging.info(f"Calculating center frequency between {start_freq} and {end_freq} MHz")
    return (start_freq + end_freq) / 2

def validate_bandwidth(bandwidth):
    if bandwidth is None:
        logging.warning("bandwidth parameter is None")
        return False
    logging.debug(f"Validating bandwidth: {bandwidth} MHz")
    return bandwidth > 0
