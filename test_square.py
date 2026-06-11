import pytest
from square import sqr

def test_positive():
    assert sqr(2) == 4
    assert sqr(3) == 9

def test_negative():
    assert sqr(-2) == 4
    assert sqr(-3) == 9
    
def test_zero():
    assert sqr(0) == 0

def test_str():
    with pytest.raises(TypeError):
        sqr("cat")