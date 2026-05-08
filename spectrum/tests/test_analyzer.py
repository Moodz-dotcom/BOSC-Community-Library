import pytest
from spectrum.analyzer import calculate_center_frequency, validate_bandwidth

def test_calculate_center_frequency():
    assert calculate_center_frequency(2400, 2483.5) == 2441.75

def test_validate_bandwidth():
    assert validate_bandwidth(20) == True
    assert validate_bandwidth(None) == False
