import pytest
from part1 import calculate_interest

def test_tier1():
    assert calculate_interest(0) == "0.00"
    assert calculate_interest(500) == "15.00"
    assert calculate_interest(1000) == "30.00"

def test_tier2():
    assert calculate_interest(1001) == "30.04"
    assert calculate_interest(6000) == "205.00"
    assert calculate_interest(11000) == "380.00"

def test_tier3():
    assert calculate_interest(11001) == "380.04"
    result = calculate_interest(50000)
    assert result == f"{(1000*0.03 + 10000*0.035 + 39000*0.04):.2f}"

def test_tier4():
    result = calculate_interest(200000)
    assert result == f"{(1000*0.03 + 10000*0.035 + 89000*0.04 + 100000*0.045):.2f}"

def test_return_type():
    assert isinstance(calculate_interest(1000), str)

def test_decimal_places():
    result = calculate_interest(500)
    assert len(result.split(".")[1]) == 2

def test_string_error():
    with pytest.raises(ValueError):
        calculate_interest("1000")

def test_bool_error():
    with pytest.raises(ValueError):
        calculate_interest(True)

def test_negative_error():
    with pytest.raises(ValueError):
        calculate_interest(-10)
