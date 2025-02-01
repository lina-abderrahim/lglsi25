import pytest
from prime_checker import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(20) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False

