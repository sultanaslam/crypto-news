import json
import requests
from django.shortcuts import render

def home(req):
    price_resp = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETC,XRP,BCH,EOS,LTC,XLM,ADA,USDT,TRX&tsyms=USD')
    price = json.loads(price_resp.content)
    api_resp = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_resp.content)
    return render(req, 'home.html', { 'api': api, 'price':price })

def prices(req):
    crypto, quote = {}, ""
    if req.method == 'POST':
        quote = req.POST['quote'].upper()
        crypto_resp = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD')
        crypto = json.loads(crypto_resp.content)
    return render(req,'prices.html', {'quote': quote, "crypto": crypto})