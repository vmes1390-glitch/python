import pytest
from countLetters import count

def test():
    assert count("hello") == 5
    assert count("python") == 6
    assert count("a") == 1
    assert count("") == 0