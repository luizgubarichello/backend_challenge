# Backend Challenge 20220626

Este é um projeto em Python e Django que faz o scraping da página do Open Food Facts uma vez ao dia e importa os produtos para um banco de dados. O projeto também expõe uma REST API para consultar os produtos importados.

## Tecnologias usadas

- Python
- Django
- Django REST Framework
- Requests
- BeautifulSoup
- Django Crontab

## Como instalar e usar

Para instalar e usar este projeto, siga os seguintes passos:

1. Clone este repositório

2. Instale as dependências do projeto:
`pip3 install -r requirements.txt`

3. Faça as migrações do banco de dados:
`python3 manage.py migrate`

4. Adicione cronjobs do seu sistema operacional:
`python3 manage.py crontab add`

5. Rode o servidor de desenvolvimento:
`python3 manage.py runserver`

6. Acesse a API no navegador ou em algum cliente HTTP:

- http://localhost:8000/ para ver a mensagem da home
- http://localhost:8000/products/3661112502850/ para ver os detalhes de um produto pelo código
- http://localhost:8000/products/ para ver a lista de todos os produtos

## Raciocínio para resolução

1. Criar um projeto com o Django por meio do comando `django-admin startproject fullstack_challenge`

2. Criar um app para o projeto via `python manage.py startapp products` e instalar em `settings.py`

3. Criar o modelo de dados em `models.py` seguindo o arquivo `products.json` como referencia para os campos necessarios

4. Fazer a migracao dos modelos para SQL por meio das migracoes do Django via `python manage.py makemigrations` e `python manage.py migrate`

5. Instalar o Django REST Framework em `settings.py`

6. Criar um serializer para o modelo de produto (`serializers.py`)
 
7. Criar as views para os endpoints da API, baseadas nas especificaoes do projeto em `views.py`

8. Criar as rotas para os endpoints em `urls.py`

9. Criar o sistema de atualização que vai realizar o scraping da página do Open Food Facts e importar os produtos para o banco de dados (`tasks.py`) <- Essa foi a parte mais trabalhosa do projeto

10. Configurar o sistema de agendamento `django.contrab` que vai executar essa função uma vez por dia, instalando `django_crontab` em `settings.py` e definindo uma lista de `CRONJOBS`

11. Criar os conjobs no SO via `python manage.py crontab add`

Assim as funcionalidades principais do projeto foram concluidas.

Para os extras:

1. Gerar a documentação da API utilizando o conceito de Open API 3.0 por meio da biblioteca [DRF OpenAPI 3](https://drf-spectacular.readthedocs.io/en/latest/readme.html#installation) -> rota utilizada para ver a documentacao = `/docs`.

2. Escrever os testes unitários para os endpoints da API -> a biblioteca `pytest` sera utilizada para isso, onde os testes estao escritos no arquivo `tests.py` da pasta do app `products`. Para executar os testes usando o pytest, basta usar o comando `pytest` na raiz do projeto.

>  This is a challenge by [Coodesh](https://coodesh.com/)