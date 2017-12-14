from django.http import HttpResponse
import json, requests

def index(request):
    url = 'https://poloniex.com/public?command=returnTicker'
    resp = requests.get(url)
    data = json.loads(resp.text)
    for d in data:
        if d=="USDT_BTC":
            answer = d + " is " + data[d]["last"]

    return HttpResponse("hello? " +  answer)