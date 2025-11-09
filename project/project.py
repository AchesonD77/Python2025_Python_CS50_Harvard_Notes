
"""
IoT Data Inspector & Query Tool
--------------------------------
- Scans files named like: chunk_YYYY-MM-DD_HH.txt
- Inspection: days covered, date range, and per-day missing hours
- Query:
    - Date only (YYYYMMDD or YYYY-MM-DD): return selected fields for all 24 hours
    - Date + hours (e.g., "3:00, 16:00"): return selected fields for those hours
    - If no fields specified, return the entire file content for the target scope

"""

from __future__ import annotations
import re
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime, date

FILENAME_RE = re.compile(
    r"^chunk_(\d{4})-(\d{2})-(\d{2})_(\d{2})\.txt$"
)

# ---------- Utility parsing ----------

def parse_date_string(s: str) -> date:
    """
    parse 'YYYYMMDD' or 'YYYY-MM-DD' to date.
    """
    s = s.strip()
    if re.fullmatch(r"\d{8}", s):
        return datetime.strptime(s, "%Y%m%d").date()
    return datetime.strptime(s, "%Y-%m-%d").date()


def parse_hours_string(s: str) -> List[int]:
    """
    Parse hours list like: '3:00, 16:00, 21' -> [3,16,21]
    Accepts '03', '3', '03:00', '3:00' etc.
    """
    hours: List[int] = []
    for token in [t.strip() for t in s.split(",")]:
        if not token:
            continue
        m = re.match(r"^(\d{1,2})(?::?\s*00)?$", token)
        if not m:
            raise ValueError(f"Invalid hour token: {token}")
        h = int(m.group(1))
        if not (0 <= h <= 23):
            raise ValueError(f"Hour out of range: {h}")
        hours.append(h)
    # de-duplicate but keep order
    seen = set()
    out = []
    for h in hours:
        if h not in seen:
            out.append(h)
            seen.add(h)
    return out


def normalize_field_name(name: str) -> str:
    """
    Normalize a metric/field name to canonical key.
    Accepts case-insensitive and CO₂/CO2/C02 variants.
    Supported:
      temperature, humidity, ieq (or 'ieq median'), co2, pm25, illuminance
    """
    n = name.strip().lower()
    # co2 variants
    n = n.replace("co₂", "co2").replace("c02", "co2")
    n = n.replace("ieq median", "ieq").replace("ieq (median)", "ieq")
    n = n.replace("pm 2.5", "pm2.5").replace("pm 2,5", "pm2.5")
    mapping = {
        "temperature": "temperature",
        "humidity": "humidity",
        "ieq": "ieq",
        "co2": "co2",
        "pm2.5": "pm25",
        "illuminance": "illuminance",
    }
    # find best match by prefix in mapping keys
    for k, v in mapping.items():
        if n.startswith(k):
            return v
    # try equals
    return mapping.get(n, n)


# ---------- Indexing ----------

@dataclass
class ChunkIndex:
    # date_str -> hour -> filepath
    by_date: Dict[str, Dict[int, str]] = field(default_factory=dict)

    def add(self, date_str: str, hour: int, path: str) -> None:
        self.by_date.setdefault(date_str, {})[hour] = path

    @property
    def day_count(self) -> int:
        return len(self.by_date)

    def date_range(self) -> Tuple[str, str]:
        if not self.by_date:
            return ("N/A", "N/A")
        days = sorted(self.by_date.keys())
        first = days[0]
        last = days[-1]
        # Earliest hour of first, latest hour of last
        first_h = min(self.by_date[first].keys())
        last_h = max(self.by_date[last].keys())
        start = f"{first} {first_h:02d}:00"
        end = f"{last} {last_h:02d}:59"
        return start, end

    def missing_hours(self, date_str: str) -> List[int]:
        have = set(self.by_date.get(date_str, {}).keys())
        return [h for h in range(24) if h not in have]


def index_chunks(folder: str) -> ChunkIndex:
    idx = ChunkIndex()
    for name in os.listdir(folder):
        m = FILENAME_RE.match(name)
        if not m:
            continue
        yyyy, mm, dd, hh = m.groups()
        date_str = f"{yyyy}-{mm}-{dd}"
        hour = int(hh)
        full = os.path.join(folder, name)
        idx.add(date_str, hour, full)
    return idx


# ---------- Parsing a chunk file ----------

FIELD_PATTERNS = {
    "temperature": re.compile(r"^temperature:\s*(.+)$", re.I),
    "humidity": re.compile(r"^humidity:\s*(.+)$", re.I),
    "ieq": re.compile(r"^ieq(?:\s*median)?:\s*(.+)$", re.I),
    "co2": re.compile(r"^co[2₂o]:\s*(.+)$", re.I),
    "pm25": re.compile(r"^pm\s*2\.?5:\s*(.+)$", re.I),
    "illuminance": re.compile(r"^illuminance:\s*(.+)$", re.I),
}

def parse_chunk_text(text: str) -> Dict[str, str]:
    """
    Return dict with canonical keys if found in the text.
    Values are the text following the field label (string).
    Also includes the raw text as 'raw'.
    """
    out: Dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        for key, pat in FIELD_PATTERNS.items():
            m = pat.match(line)
            if m and key not in out:
                out[key] = m.group(1).strip()
    out["raw"] = text.strip()
    return out


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ---------- Queries ----------

def query_day(idx: ChunkIndex, date_str: str, fields: Optional[List[str]] = None) -> Dict[int, Dict[str, str]]:
    """
    Return mapping hour -> {field:value} (or full 'raw' if fields is None).
    Missing hours are not included.
    """
    by_hour = idx.by_date.get(date_str, {})
    result: Dict[int, Dict[str, str]] = {}
    for h in sorted(by_hour.keys()):
        data = parse_chunk_text(read_file(by_hour[h]))
        if fields:
            sub = {}
            for f in fields:
                key = normalize_field_name(f)
                if key in data:
                    sub[key] = data[key]
            result[h] = sub
        else:
            result[h] = {"raw": data["raw"]}
    return result


def query_hours(idx: ChunkIndex, date_str: str, hours: List[int], fields: Optional[List[str]] = None) -> Dict[int, Dict[str, str]]:
    result: Dict[int, Dict[str, str]] = {}
    for h in sorted(hours):
        path = idx.by_date.get(date_str, {}).get(h)
        if not path:
            result[h] = {"error": "file not found"}
            continue
        data = parse_chunk_text(read_file(path))
        if fields:
            sub = {}
            for f in fields:
                key = normalize_field_name(f)
                if key in data:
                    sub[key] = data[key]
            result[h] = sub
        else:
            result[h] = {"raw": data["raw"]}
    return result


# ---------- Reporting ----------

def inspection_report(idx: ChunkIndex) -> str:
    lines: List[str] = []
    lines.append("=== Inspection Report ===")
    lines.append(f"Days covered: {idx.day_count}")
    start, end = idx.date_range()
    lines.append(f"Date range: {start} -> {end}")
    lines.append("Per‑day completeness (missing hours listed):")
    for d in sorted(idx.by_date.keys()):
        miss = idx.missing_hours(d)
        if miss:
            lines.append(f"  {d}: missing {', '.join(f'{h:02d} hour file' for h in miss)}")
        else:
            lines.append(f"  {d}: complete (24/24)")
    # Also include dates that appear due to gaps? (Not applicable without a calendar source)
    return "\n".join(lines)


def format_query_output_day(result: Dict[int, Dict[str, str]], fields: Optional[List[str]]) -> str:
    lines: List[str] = []
    for h in range(24):
        if h not in result:
            continue
        lines.append(f"[{h:02d}:00]")
        if fields:
            for k, v in result[h].items():
                lines.append(f"  {k}: {v}")
        else:
            lines.append(result[h].get("raw", ""))
        lines.append("")
    return "\n".join(lines).strip()


def format_query_output_hours(result: Dict[int, Dict[str, str]], fields: Optional[List[str]]) -> str:
    lines: List[str] = []
    for h in sorted(result.keys()):
        lines.append(f"[{h:02d}:00]")
        row = result[h]
        if "error" in row:
            lines.append(f"  ERROR: {row['error']}")
        else:
            if fields:
                for k, v in row.items():
                    lines.append(f"  {k}: {v}")
            else:
                lines.append(row.get("raw", ""))
        lines.append("")
    return "\n".join(lines).strip()


# ---------- CLI main ----------

def main() -> None:
    print("IoT Data Inspector & Query Tool")
    folder = input("Data folder (where chunk_YYYY-MM-DD_HH.txt lives): ").strip() or "."
    idx = index_chunks(folder)
    while True:
        print("\n" + "-" * 20)
        print("Choose mode:")
        print("  1) Inspect")
        print("  2) Query")
        print("  q) Quit")
        choice = input("> ").strip().lower()
        if choice == "1":
            print(inspection_report(idx))
        elif choice == "2":
            date_in = input("Date (YYYYMMDD or YYYY-MM-DD): ").strip()
            try:
                d = parse_date_string(date_in)
            except Exception as e:
                print(f"Invalid date: {e}")
                continue
            date_str = d.strftime("%Y-%m-%d")
            hours_in = input("Hours (e.g., '3:00, 16:00') or blank for whole day: ").strip()
            fields_in = input("Fields (comma, case-insensitive; e.g. 'Temperature, CO2, IEQ median') or blank for ALL: ").strip()
            fields = [f.strip() for f in fields_in.split(",")] if fields_in else None
            if hours_in:
                try:
                    hours = parse_hours_string(hours_in)
                except Exception as e:
                    print(f"Invalid hours: {e}")
                    continue
                result = query_hours(idx, date_str, hours, fields)
                print(format_query_output_hours(result, fields))
            else:
                result = query_day(idx, date_str, fields)
                print(format_query_output_day(result, fields))
        elif choice in ("q", "quit", "exit"):
            break
        else:
            print("Unknown choice.")

if __name__ == "__main__":
    main()
