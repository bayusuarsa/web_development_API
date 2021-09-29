import requests

# symbols = input("Symbols : ")
url = "http://api.marketstack.com/v1/tickers?"
params = {
    "access_key": "84ff9226e6ae854bc448f2de0157bde5",
    # "symbols": symbols
}

response = requests.get(url=url, params=params)
data = response.json()["data"][0]
print(data)