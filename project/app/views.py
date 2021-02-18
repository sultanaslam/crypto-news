from django.shortcuts import render

def home(req):
    import json
    import requests
    api_resp = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_resp.content)
    return render(req, 'home.html', { 'api': api })