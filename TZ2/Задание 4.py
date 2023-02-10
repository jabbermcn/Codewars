import requests


def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']


print(get_public_ip())
