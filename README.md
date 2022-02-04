Django-2.0-Fundamentos
======================
Repositório destinado a estudo aplicação de framework Django através do curso Django 2.0 Fundamentos

## Prepação do ambiente

### Criação do ambiente

Comando no terminal:<br>
```python3 -m venv env-fundamentos```

### Ativação  do ambiente

Comando no terminal:<br>
```source env-fundamentos/bin/activate```

### Instalação de pacotes necessários

Comando no terminal:<br>
```pip3 install -r requirements.txt```

## Projeto Django
### Iniciando um projeto Django
- Com o ambiente virtual ativado, seguir o seginte código no terminal de comando:<br>
```django-admin startproject controle_despesas```
- Esse projeto terá nome de "controle_depesas"
## Rodando a primeira app no Django
### Criação da app
comando no terminal:<br>
```python3 manage.py startapp contas```
- Aqui criará uma aplicação com o nome 'contas'

### Cadastro da app
O cadastro é no _settings.py_ do projeto(aqui chamado de _controle despesas_) e adicionar o nome da nova app criada(_contas_).
```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...,

    ...,
    'contas',
]
```
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
### Pré-âmbulo da composilçao da nova tabela
 após criação do models é necessário aplicá-los no migrations, o qual indicará para o Django como dever ser criado o banco de dados.
 -Após parar o servidor, caso esteja rodando. 
 
Comando no terminal:<br>
```python manage.py makemigrations```
### Criação da tabela
<p>Após a descrição de como deve ser gerados a tabela de dados, a aplicação da tabela no projeto deve ser feita.</p>

Comando no terminal:<br>
```python manage.py migrate```

### Testar a presença da nova tabela
1.Um modo de testar a nova tabela é registrá-la no _admin.py_ de minha aplicação

```
from .models import Categoria

admin.site.register(Categoria)
```
2.Acessar o server via admin
Comando no terminal:<br>
```python manage.py runserver```
- Verificar qual porta está para acessar o admin e verificar se há _Categorias_ no app _Contas_

### Integração com diferentes tabelas
1. Criação no models:

```
class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observacoes = models.TextField(null=True,blank=True)
```


 - Criação de uma nova tabela 'Transacoes' que irá receber ForeignKey da tabela categoria
 - ```categoria``` irá receber a informação da tabela 'Categoria'
2. Pré-âmbulo
Comando no terminal:<br>
```python manage.py makemigrations```
- criação da tabela em si 
Comando no terminal:<br>
```python manage.py migrate```
3. Registro na aplicação no no _admin.py_ 
```
from .models import Transacoes

admin.site.register(Transacoes)
```
4. Acessar o server via admin
Comando no terminal:<br>
```python manage.py runserver```

### Representação na web aplicação
1. [Meta](https://docs.djangoproject.com/en/4.0/ref/models/options/)
 <p>Para alterar algumas opções da representação de objetos/classe é possível usar meta</p>

``` 
class Meta:
        verbose_name_plural = 'Transações'
```
 - Aqui, alterando o nome do model ao ter mais de um

2. [Métodos Mágicos](https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html)
 <p>Também,relacionado como representar um objeto de classe, pode-se utilizar método mágico para alterar sua observação.</p>

```
    def __str__(self):
        return self.descricao
```
- Aqui, a represetação da transação será o próprio atributo ```descricao```

## Mais sobre os sistemas de templates
### Sobre o Jinja
 [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/) é um mecanismo de modelagem rápido, expressivo e extensível. Espaços reservados especiais no modelo permitem escrever código semelhante à sintaxe do Python. Em seguida, o modelo recebe dados para renderizar o documento final.

### Definindo as variáveis na views
 Para utilização do jinja e perfomar o comportamento de atributos e objetos deve-se definir primeiramente as variáveis
na _view.py_ e aplicálas no ```render```:
```
def home(request):
    data = {}
    data['transacoes'] = ['t1' , 't2' , 't3']
    data['now'] = datetime.datetime.now()

    return render(request, 'contas/home.html', data)
```
- Aqui a variável de manipulação será o dicionário ```data```, o qual terá as keys _'transacoes'_ e _'now'_ para manipulação no jinja.

### A utilização do jinja no template
 No template, o valor da variável se obtem através chaves duplas'{{}}' e sua manipulação com diferentes operações acontece via chaves simples '{}':

``` 
<body>
    ...
    <p>Agora são: {{ now }} </p>
    <ul>
        {% for item in transacoes %}
            {% if item == "t2" %}
            <li><b>{{ item }}</b></li>
            {% else %}
            <li>{{ item }}</li>
            {% endif %}
        {% endfor %}
    </ul>
    ...
</body>
```
- Diferente do python nativo, deve-se se indicar o fim de operações de condição e laço de repetição, como ```{% endfor %}```;
- O sintaxe de operadoes de comparação deve conter strings com aspas duplas como o caso do ```"t2"```