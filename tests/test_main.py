import pytest
import math

def calculate_compound_interest(investment, interest_rate):
    return investment * math.pow((1 + interest_rate / 100), 10)

def test_calculate_compound_interest():
    investment = 1000
    interest_rate = 5
    expected_result = 1638.62
    assert round(calculate_compound_interest(investment, interest_rate), 2) == expected_result

def test_calculate_compound_interest_zero_investment():
    investment = 0
    interest_rate = 5
    expected_result = 0
    assert calculate_compound_interest(investment, interest_rate) == expected_result

def test_calculate_compound_interest_zero_interest_rate():
    investment = 1000
    interest_rate = 0
    expected_result = 1000
    assert calculate_compound_interest(investment, interest_rate) == expected_result

def test_calculate_compound_interest_negative_investment():
    investment = -1000
    interest_rate = 5
    with pytest.raises(ValueError):
        calculate_compound_interest(investment, interest_rate)

def test_calculate_compound_interest_negative_interest_rate():
    investment = 1000
    interest_rate = -5
    with pytest.raises(ValueError):
        calculate_compound_interest(investment, interest_rate)
