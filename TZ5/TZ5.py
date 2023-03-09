import requests
import time
import json


def get_eth_price():
    url = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    params = {'symbol': 'ETHUSDT'}
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    eth_price = float(data['lastPrice'])
    print(eth_price)
    return eth_price


def check_price_change():
    start_price = get_eth_price()
    time.sleep(5)
    end_price = get_eth_price()
    price_change = (end_price - start_price) / start_price * 100
    print(price_change)
    return price_change


while True:
    price_change = check_price_change()
    if abs(price_change) > 1:
        print(f"Price change: {price_change:.2f}%")
    time.sleep(5)
