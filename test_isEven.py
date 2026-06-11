import pytest
from isEven import isE

def test():
    assert isE(2) == True
    assert isE(4) == True
    assert isE(7) == False
    assert isE(15) == False
    assert isE(0) == True