import pytest
from jar import Jar

def test_init_and_accessors():
    j = Jar(10)
    assert j.capacity == 10
    assert j.size == 0

def test_init_rejects_bad_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_str_and_deposit():
    j = Jar(5)
    j.deposit(3)
    assert str(j) == "🍪🍪🍪"
    assert j.size == 3
    j.deposit(2)
    assert str(j) == "🍪🍪🍪🍪🍪"

def test_deposit_overflow_raises():
    j = Jar(4)
    j.deposit(4)
    with pytest.raises(ValueError):
        j.deposit(1)

def test_withdraw_and_underflow():
    j = Jar(6)
    j.deposit(4)
    j.withdraw(1)
    assert j.size == 3
    with pytest.raises(ValueError):
        j.withdraw(5)  # more than available

def test_reject_negative_operations():
    j = Jar(3)
    with pytest.raises(ValueError):
        j.deposit(-1)
    with pytest.raises(ValueError):
        j.withdraw(-1)
