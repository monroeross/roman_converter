import pytest
from src.roman_converter import Wang_a, Wang_b, Wang_c

@pytest.mark.parametrize("impl, name", [
    (Wang_a, "Implementation_A"),
    (Wang_b, "Implementation_B"),
    (Wang_c, "Implementation_C"),
])
def test_roman_isp(impl, name):
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(15) == "XV"
    
    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    assert impl.to_roman(90) == "XC"
    
    assert impl.to_roman(3999) == "MMMCMXCIX"