import requests
import json
import sys

try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    if len(sys.argv) == 2:
        arg = float(sys.argv[1])
        r = requests.get(url)
        j = r.json()
        rate = j["bpi"]["USD"]["rate_float"]
        amount = arg*rate
        print(f"${amount:,.4f}")
    else:
        print("Missing command-line argument")
        sys.exit(1)


except requests.RequestException:
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number.")
    sys.exit(1)