
import os
from pathlib import Path
import textwrap

import project

SAMPLE = """Data: 2025-09-11
Hour range: 01:00 - 02:00

Temperature: median 27.4°C, max 27.4°C, min 27.3°C
Humidity: median 49.8%
IEQ median: 63 (poor)
CO₂: 428–438 ppm (optimal)
PM2.5: 4.7 µg/m³ (good)
illuminance: median 0 lux
"""


def test_parse_date_string():
    assert project.parse_date_string("20250823").isoformat() == "2025-08-23"
    assert project.parse_date_string("2025-08-23").isoformat() == "2025-08-23"


def test_parse_hours_string():
    assert project.parse_hours_string("3:00, 16:00, 03") == [3, 16]
    assert project.parse_hours_string("0,23") == [0, 23]


def test_normalize_field_name():
    assert project.normalize_field_name("CO₂") == "co2"
    assert project.normalize_field_name("C02") == "co2"
    assert project.normalize_field_name("ieq median") == "ieq"
    assert project.normalize_field_name("PM 2.5") == "pm25"


def test_parse_chunk_text():
    data = project.parse_chunk_text(SAMPLE)
    assert data["temperature"].startswith("median 27.4")
    assert data["humidity"].startswith("median 49.8")
    assert data["ieq"].startswith("63")
    assert data["co2"].startswith("428")
    assert data["pm25"].startswith("4.7")
    assert "raw" in data


def _make_file(dir: Path, name: str, body: str) -> None:
    (dir / name).write_text(body, encoding="utf-8")


def test_index_and_missing_hours(tmp_path: Path):
    # create two days with partial coverage
    day1 = ["chunk_2025-08-10_00.txt", "chunk_2025-08-10_01.txt"]
    day2 = ["chunk_2025-08-11_03.txt"]
    for n in day1 + day2:
        _make_file(tmp_path, n, SAMPLE)

    idx = project.index_chunks(str(tmp_path))
    assert idx.day_count == 2
    # day1 missing 22 hours (2 present)
    assert len(idx.missing_hours("2025-08-10")) == 22
    # day2 missing 23 hours (1 present)
    assert len(idx.missing_hours("2025-08-11")) == 23


def test_query_day_and_hours(tmp_path: Path):
    _make_file(tmp_path, "chunk_2025-08-11_01.txt", SAMPLE)
    idx = project.index_chunks(str(tmp_path))

    res_day = project.query_day(idx, "2025-08-11", fields=["Temperature","CO2"])
    assert 1 in res_day and "temperature" in res_day[1] and "co2" in res_day[1]

    res_hours = project.query_hours(idx, "2025-08-11", [1], fields=None)

