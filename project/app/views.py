from django.shortcuts import render

def home(req):
    import json
    import requests
    price_resp = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD')
    price = json.loads(price_resp.content)
    api_resp = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_resp.content)
    return render(req, 'home.html', { 'api': api, 'price':price })