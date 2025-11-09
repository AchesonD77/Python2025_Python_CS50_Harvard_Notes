# IoT Data Inspector & Query Tool
*CS50 Final Project — Python*

#### Video Demo: <URL HERE>
#### Short URL: <URL HERE>
#### Author: Dan (Acheson Dan)

---

## Overview
**What it is.** 
- A small, testable **CLI** program that scans hourly IoT text files named like `chunk_YYYY-MM-DD_HH.txt`, checks dataset completeness (24 hours per day), and lets you **query** either the whole day or specific hours for key fields: *Temperature, Humidity, IEQ median, CO₂/CO2/C02, PM2.5, Illuminance* (case-insensitive).

**Why.** 
- In real-world IoT workflows, we often collect one text file per hour and later need consistent **inspection** and **retrieval** over flexible time windows. This tool mirrors that pattern while remaining pure Python.

**Key features.**
- Dataset inspection: covered days, overall date range, and **per-day missing hours** list.
- Date parsing: accepts `YYYYMMDD` or `YYYY-MM-DD`.
- Hour parsing: `3`, `03`, `3:00`, `03:00` (comma-separated; deduplicated).
- Field normalization: maps variants like `CO₂/C02/CO2`, `IEQ median`, `PM 2.5` to canonical keys.
- No external dependencies; easy grading.

---

## File & Folder Structure
```
project.py         # main() + core functions (parsing, indexing, querying, reporting)
test_project.py    # pytest unit tests
requirements.txt   # library
data/              # (chunk_YYYY-MM-DD_HH.txt files)
```

### Chunk filename rule
`chunk_YYYY-MM-DD_HH.txt` (e.g., `chunk_2025-09-11_01.txt`)

### Sample chunk content (free-form, one field per line)
```
Data: 2025-09-11
Hour range: 01:00 - 02:00

Temperature: median 27.4°C, max 27.4°C, min 27.3°C
Humidity: median 49.8%
IEQ median: 63 (poor)
CO₂: 428–438 ppm (optimal)
PM2.5: 4.7 µg/m³ (good)
illuminance: median 0 lux
```

---

## How to Run / Usage
1. Put your chunk files in a folder (or use the current directory).
2. Run:
   ```bash
   python project.py
   ```
3. Choose:
   - **1) Inspect** → prints days covered, date range, per-day missing hours.
   - **2) Query** →
     - **Date**: `20250911` or `2025-09-11`
     - **Hours**: e.g., `3:00, 16:00` or leave blank for whole day
     - **Fields**: e.g., `Temperature, CO2, IEQ median` or leave blank to return raw text

**Examples**:
- Whole day with selected fields:
  - Date: `2025-09-11`, Hours: *(blank)*, Fields: `Temperature, CO2`
- Specific hours, raw content:
  - Date: `2025-09-11`, Hours: `1:00, 16:00`, Fields: *(blank)*

---

## How it Works
- **Index** (/ˈɪndɛks/) build: scan folder → map `date → hour → path`.  
- **Regex** (/ˈriːɡɛks/) parsers: one per field; capture text after the colon.  
- **Normalization**: `CO₂/C02/CO2` → `co2`; `IEQ median` → `ieq`; `PM 2.5` → `pm25`.  
- **Separation of concerns**: query functions return dicts; formatting functions render CLI blocks.  
- **Robustness**: clear error for missing hour (`ERROR: file not found`), friendly messages for invalid date/hour tokens.

Core functions (selection):
- `parse_date_string`, `parse_hours_string`, `normalize_field_name`
- `index_chunks`, `ChunkIndex.missing_hours`, `date_range`
- `parse_chunk_text`
- `query_day`, `query_hours`
- `inspection_report`

---

## Testing (pytest)
Run:
```bash
pytest -q
```
Covers: date/hour parsing, field normalization, text parsing, indexing completeness, and day/hour queries (including missing-hour behavior).

---

## Future Work
- Extract numeric medians/max/min for charts/CSV export.
- Natural-language time windows (“midnight to daybreak”) on top of exact hours.
- Configurable IEQ weighting; thresholds & alarms via YAML rules.
- Optional `pydantic` validation and richer CLI (subcommands).

---

*This project is intentionally small but realistic, emphasizing clean parsing, clear error handling, and testability*

*You can use it to query, inspect, check your IOT data files, and also get and search data information from your files.*
