"""
To achieve that, we:
Read the number of bitcoins (n) from the command line.
Call an API (Application Programming Interface) on the internet to get the latest Bitcoin price.
Multiply n × price and print the result beautifully formatted.

1. Imports — Bringing Tools into Scope
import
os: lets us interact with the operating system (e.g., environment variables).
syssys.argvsys.exitsys: gives us access to command-line arguments (sys.argv) and allows clean program exit (sys.exit).
requestsrequests: an external library for making HTTP requests easily.
Instead of using the complex built-in urllib, we use requests.get().

2. Constants — Global Setup
API_URL = "https://rest.coincap.io/v3/assets/bitcoin"
API_KEY = "cc58bc9c493a77de47007c140ebbf78d0d64714ab60a123343cb99d64b024510"
API_URLAPI_URL is the endpoint we’ll call to get Bitcoin data.
API_KEYAPI_KEY is your personal identifier — the service uses it to know who you are.
In real projects, we keep this secret in an environment variable, but here it’s hard-coded for simplicity.

sys.argv[0]sys.argv[0] → program name
sys.argv[1]sys.argv[1] → the string "2.5""2.5"

include thousands separators (12345 → 12,345)
.4f → show exactly 4 digits after the decimal

requests.get()
Sends an HTTP GET request to API_URL.
Adds apiKey=YOUR_KEY to the URL parameters.
Waits up to 10 seconds (timeout).

r.raise_for_status()
Automatically raises an error for 4xx or 5xx HTTP codes (bad responses).
This saves you from having to check if r.status_code != 200: manually.

payload = r.json()
Converts the returned JSON text (e.g., {"data": {"priceUsd": "68000.34"}})
into a Python dictionary.

RequestExceptionRequestException: network failures (no Wi-Fi, bad URL, timeout).
ValueErrorValueError: converting strings to floats fails.
KeyErrorKeyError: expected keys missing from JSON.
Using sys.exit() is polite; it terminates the program with a readable message.
"""

import os
import sys
import requests

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"


def main():
    # 1) read how many BTC from the CLI
    n = parse_amount_from_cli(sys.argv)

    # 2) load API key from environment (never hardcode secrets)
    api_key = get_api_key()

    # 3) call API → get current BTC price in USD (float)
    price_usd = fetch_btc_price_usd(api_key)

    # 4) compute & print with commas + 4 decimals
    total = n * price_usd
    print(f"${total:,.4f}")


def parse_amount_from_cli(argv) -> float:
    """Return float amount from CLI or exit with a helpful message."""
    if len(argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        return float(argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_api_key() -> str:
    """Read API key from env var; exit if missing."""
    key = os.environ.get("COINCAP_API_KEY")
    if not key:
        sys.exit("Missing COINCAP_API_KEY")
    return key


def fetch_btc_price_usd(api_key: str) -> float:
    """Query CoinCap v3 and return priceUsd as a float."""
    try:
        r = requests.get(API_URL, params={"apiKey": api_key}, timeout=10)
        r.raise_for_status()                      # 4xx/5xx → exception
        payload = r.json()                        # JSON → dict

        # Typical v3 shape: {"data": {"priceUsd": "xxxxx.xx", ...}, ...}
        price = None
        if isinstance(payload, dict):
            data = payload.get("data")
            if isinstance(data, dict) and "priceUsd" in data:
                price = data["priceUsd"]
            elif "priceUsd" in payload:          # fallback
                price = payload["priceUsd"]

        if price is None:
            raise KeyError("priceUsd not found")
        return float(price)

    except requests.RequestException as e:
        sys.exit(f"Network error: {e}")
    except (ValueError, KeyError) as e:
        sys.exit(f"Error parsing API response: {e}")


if __name__ == "__main__":
    main()