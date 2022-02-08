from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import datetime
from .models import Transacao
from .form import TransacaoForm

def data_atual(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now:%Y/%m/%d, %H:%M:%S}.</body></html>"
    return HttpResponse(html)

def home(request):
    data = {}
    data['transacoes'] = ['t1' , 't2' , 't3']
    data['now'] = datetime.datetime.now()

    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/transacoes.html', data)

def nova_transacao(request):

    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')



    return render(request,'contas/form.html', {'form':form})