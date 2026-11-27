import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

n = 0

try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

api_key = "226026860d640c37f88756169a3b075b8af42376b65ddca7e5329f1a55a36cd0"

api_url = os.getenv("API_URL")

response = requests.get(api_url).json()

data = response["data"]
price = float(data["priceUsd"]) * n

print(f"${price:,.4f}")
