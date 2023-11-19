import requests

"""
url = "https://api.coinbase.com/v2/prices/"
query = "spot?currency="
curr = "USD"

qString = url + query + curr

r = requests.get(qString)
print(r.text)
"""

VA = ["BTC", "ETH", "USDT", "AVAX", "ATOM", "DOT", "AAVE", "LINK", "UNI"]

for va in VA:
    
    url = "https://api.coinbase.com/v2/prices/"
    pair = "-USD/"
    side = "spot"

    qString = url + va + pair + side
    r = requests.get(qString)
    print(r.text)

