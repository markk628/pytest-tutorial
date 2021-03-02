import math, pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if carbon_14_ratio <= 0:
        raise ValueError("invalid ratio")
    answer = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
    return math.floor(answer * 100)/100.0

def test_get_age_carbon_14_dating():
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34)

def test_for_value_errors():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)
        get_age_carbon_14_dating(-1)