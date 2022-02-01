# Django-2.0-Fundamentos
Repositório destinado a estudo aplicação de framework Django através do curso Django 2.0 Fundamentos

## Prepação do ambiente
###Criação do ambiente
Comando no terminal:<br>
```python3 -m venv env-fundamentos```
###Ativação  do ambiente
Comando no terminal:<br>
```source env-fundamentos/bin/activate```
###Instalação de pacotes necessários
Comando no terminal:<br>
```pip3 install -r requirements.txt```
## Projeto Django
### Iniciando um projeto Django
- Com o ambiente virtual ativado, seguir o seginte código no terminal de comando:<br>
```django-admin startproject controle_despesas```
- Esse projeto terá nome de "controle_depesas"
## Rodando a primeira app no Django
### Criação da aplicação
comando no terminal:<br>
```python3 manage.py startapp contas```
- Aqui criará uma aplicação com o nome 'contas'
### Criação do banco de dados
comando no terminal:<br>
``` python3 manage.py migrate```
- Criará o banco de dados na plataforma sqlite3, default do Django, outras opções estão disponíveis na documentação no Django(presente no settings)
### Execução local da aplicação
comando no terminal:<br>
``` python3 manage.py runserver```
- O terminal estará rodando o servidor da aplicação, verificar se está 'okay' via endereço-porta a apresentada no terminal.
- O comando 'Crtl+C' para a execução do servidor
### Criação de superuser
Também visto como _admin_, é necessário para manipulação com 'superpoderes' da aplicação.
comando no terminal:<br>
```python3 manage.py createsuperuser```
- Após rodar novamente a aplicação, verificar nos URL's o endereço de acesso para superuser
## Views e URL's no Django
A própria a [documentação](https://docs.djangoproject.com/en/4.0/topics/http/views/) do Django exemplifica uma utlização de view.
### criação da view
- Código sobre o arquivo <em>views.py</em>:
``` from django.http import HttpResponse
import datetime

def data_atual(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now:%Y/%m/%d, %H:%M:%S}.</body></html>"
    return HttpResponse(html)
```
    
### Implemenação da URL
Código sobre o arquivo _urls.py_ na pasta _controle_despesas_:
```from django.contrib import admin
from django.urls import path
from contas.views import data_atual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste_views/', data_atual),
]
```
-  Pode-se verificar a alteração acessando a url _'teste_views/'_ na porta de execução do Django.

## Utilização de templates 
1.Inicialmente, cria-se o view que utilizará o template 
```
def home(request):
    return render(request, 'contas/home.html')
```

2.Criação da pasta templates onde na própria, aqui colocado no caminho _/contas/templates_

3.Criação do template:
<p>Para criar um novo template basta criar um arquivo html, aqui nomeado como <em>home.html</em></p>
<p>No arquivo, digitar -> html:5 + <button>TAB</button>.<p></p>

4.Para configuração onde utilizar templates, basta ir em _settings.py_ e colocar o caminho do [diretório dos templates](https://docs.djangoproject.com/pt-br/3.0/howto/overriding-templates/)
Implentar a url da nova view para testar no servidor.

Obs: Dado mudanças no projeto(arquivo _settings.py_) é necessário reiniciar o servidor para testar a nova view.

## Models
### Criação de Models
<p>Models pode ser explicado como descrição de como será o banco de dados</p>
1. criar uma classe com herança da classe model no arquivo _models.py_

``` 
class Categoria(models):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
```
 - Nova tabela cujo nome categoria, [aqui](https://docs.djangoproject.com/en/4.0/ref/models/fields/) pode saber mais sobre os fields do django
### Atualização do migrations
 após criação do models é necessário aplicá-los no migrations, o qual indicará para o Django como dever ser criado o banco de dados.
 -Após parar o servidor, caso esteja rodando.
 comando no terminal:<br>
```python manage.py makemigrations```