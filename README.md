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
