import pytest
from calculator import sum
from calculator import sub 

def test_sum():
    assert sum(2, 3) == 5
    assert sum(0, 0) == 0

def test_sub():
    assert sub(10, 3) == 7
    assert sub(5, 5) == 0 