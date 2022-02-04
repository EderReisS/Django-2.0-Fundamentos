from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def data_atual(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now:%Y/%m/%d, %H:%M:%S}.</body></html>"
    return HttpResponse(html)

def home(request):
    data = {}
    data['transacoes'] = ['t1' , 't2' , 't3']
    data['now'] = datetime.datetime.now()

    return render(request, 'contas/home.html', data)