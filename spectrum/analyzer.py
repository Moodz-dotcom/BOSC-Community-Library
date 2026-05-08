# BUG #1: Off-by-one in frequency calculation
def calculate_center_frequency(start_freq, end_freq):
    # Bug: uses +1 instead of division by 2
    return (start_freq + end_freq) + 1  # WRONG

# BUG #2: No null handling
def validate_bandwidth(bandwidth):
    return bandwidth > 0  # CRASHES if bandwidth is None

def calculate_center_frequency(start_freq, end_freq):
    return (start_freq + end_freq) / 2

def validate_bandwidth(bandwidth):
    if bandwidth is None:
        return False
    return bandwidth > 0
