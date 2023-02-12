# Задание 1
# Напишите код программы на Python, которая будет в реальном времени (с максимально возможной скоростью) считывать текущую цену фьючерса XRP/USDT
# на бирже Binance.
# В случае, если цена упала на 1% от максимальной цены за последний час, программа должна вывести сообщение в консоль.
# При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.


import time
from binance.client import Client

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_SECRET_KEY'
# After registering, please make a deposit in your Spot Wallet and try again.
# Я не пользовался бинансом до этого и при попытке создать API key система просит пополнить баланс, в теории код ниже должен работать.
client = Client(api_key, api_secret)
max_price = client.get_ticker(symbol='XRPUSDT')['high']
while True:
    # Считывайте текущую цену XRP/USDT с биржи Binance
    current_price = client.get_ticker(symbol='XRPUSDT')['lastPrice']
    # Рассчитайте процентное изменение цены
    percent_change = (current_price - max_price) / max_price * 100
    # Если текущая цена упала на 1% от максимальной, выведите сообщение
    if percent_change < -1:
        print('XRP/USDT price has dropped by more than 1%. Current price is:', current_price)
    # Задержка 0.5 с, чтобы избежать «DOS-атак» на API Binance
    time.sleep(0.5)

# Задание 2
# Для обработки более одной пары валют можно использовать asyncio, разбив валюты на корутины
# и когда в конкретной корутине происходит изменение оно отображается.
