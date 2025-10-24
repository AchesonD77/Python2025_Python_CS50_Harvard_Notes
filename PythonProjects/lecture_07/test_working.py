# test_working.py
import pytest
from working import convert

# --- 1) Core conversions (examples from the spec) ---
def test_examples():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

# --- 2) Boundary minutes + hour wrap (catches "minutes off by five" & hour errors) ---
def test_boundaries_and_minutes():
    assert convert("12:01 AM to 12:59 PM") == "00:01 to 12:59"
    assert convert("11:59 PM to 12 AM") == "23:59 to 00:00"

# --- 3) Formatting mistakes must raise ValueError ---
def test_bad_formatting_raises():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")          # missing spaces around AM/PM
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")         # wrong separator
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")      # already 24-hour, not allowed by spec

# --- 4) Out-of-range values must raise ValueError ---
def test_out_of_range_raises():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")  # minutes out of range
    with pytest.raises(ValueError):
        convert("13:00 PM to 1 PM")    # hour out of range
    with pytest.raises(ValueError):
        convert("10:7 AM to 5:1 PM")   # minutes must be two digits
