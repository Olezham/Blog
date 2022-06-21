from django.shortcuts import render

from django.shortcuts import render

import requests

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()


def money_course_euro():
    for coin in response:
        if 'EUR' == coin['ccy']:
            num = float(coin['buy'])
            return round(num, 2)


def money_course_usd():
    for coin in response:
        if 'USD' == coin['ccy']:
            num = float(coin['buy'])
            return round(num, 2)


def index(request):
    return render(request, 'index.html', {'euro': money_course_euro(), 'usd': money_course_usd()})


def coding(request):
    return render(request, 'coding.html', {'euro': money_course_euro(), 'usd': money_course_usd()})



