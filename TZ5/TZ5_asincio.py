import asyncio
import requests
import json


async def get_eth_price():
    url = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    params = {'symbol': 'ETHUSDT'}
    response = await loop.run_in_executor(None, requests.get, url, params)
    data = json.loads(response.text)
    eth_price = float(data['lastPrice'])
    return eth_price


async def check_price_change():
    start_price = await get_eth_price()
    await asyncio.sleep(3600)
    end_price = await get_eth_price()
    price_change = (end_price - start_price) / start_price * 100
    return price_change


async def main():
    while True:
        price_change = await check_price_change()
        if abs(price_change) > 1:
            print(f"Price change: {price_change:.2f}%")
        await asyncio.sleep(5)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
