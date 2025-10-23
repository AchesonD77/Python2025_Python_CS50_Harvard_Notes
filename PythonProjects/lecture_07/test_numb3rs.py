from numb3rs import validate


# --- Valid addresses ---
def test_valid_basic():
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")
    assert validate("140.247.235.144")
    assert validate("0.0.0.0")


# --- Structure errors (not 4 octets, or bad punctuation) ---
def test_structure():
    assert not validate("8.8.8")              # only 3 parts
    assert not validate("10.10.10.10.10")     # 5 parts
    assert not validate("192.168.0.")         # trailing dot
    assert not validate(".192.168.0.1")       # leading dot


# --- Non-digit content ---
def test_nondigits():
    assert not validate("cat")
    assert not validate("1.2.3.a")
    assert not validate("1..2.3")             # empty octet


# --- Range checks (catch “only first byte checked” bugs) ---
def test_range_each_octet():
    assert not validate("256.0.0.1")          # first octet bad
    assert not validate("1.256.0.1")          # second octet bad
    assert not validate("1.2.300.1")          # third octet bad
    assert not validate("1.2.3.999")          # fourth octet bad


# --- Leading zeros are invalid (except single '0') ---
def test_leading_zeros():
    assert not validate("000.001.010.100")
    assert not validate("01.2.3.4")
    assert validate("0.2.3.4")                # single zero is fine
