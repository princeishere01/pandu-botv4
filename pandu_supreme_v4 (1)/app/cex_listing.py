import requests

def get_binance_new_listings():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(url)
    tokens = set()
    if response.status_code == 200:
        data = response.json()
        for symbol in data['symbols']:
            if symbol['status'] == 'TRADING':
                tokens.add(symbol['baseAsset'])
    return list(tokens)
