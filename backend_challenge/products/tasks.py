import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from . import models
import re

def hello():
    print('hello')

def scrape_products():
    # definir a URL da página inicial do Open Food Facts
    base_url = 'https://world.openfoodfacts.org/'

    # fazer uma requisição GET para a URL e obter o conteúdo HTML
    response = requests.get(base_url)
    html = response.text

    # criar um objeto BeautifulSoup para parsear o HTML
    soup = BeautifulSoup(html, 'html.parser')

    # encontrar todos os elementos <a> que tenham href com '/product/'
    links = soup.find_all('a', title=True, href=re.compile(r'^/product/'))

    # limitar a importação a somente 100 produtos
    links = links[:100]

    # percorrer cada link e obter os dados do produto
    for link in links:

        # obter a URL do produto
        product_url = base_url[:-1] + link['href']

        # fazer uma requisição GET para a URL do produto e obter o conteúdo HTML
        product_response = requests.get(product_url)
        product_html = product_response.text

        # criar um objeto BeautifulSoup para parsear o HTML do produto
        product_soup = BeautifulSoup(product_html, 'html.parser')

        # encontrar o elemento <Title> que contenha o nome do produto para inicializar o dicionario com as informacoes
        product_dict = {
            'Product Name': product_soup.find('title').text.strip(),
            'Code': int(link['href'][1:].split('/')[1]),
        }

        # encontrar o codigo de barras
        try:
            product_dict['Bar Code'] = product_soup.find('p', id='barcode_paragraph').text.split(':')[1].strip()
        except AttributeError:
            product_dict['Bar Code'] = "not found"

        # encontrar os elementos <p> que tenham o id field_
        product_details = product_soup.find_all('p', id=re.compile(r'^field_'))

        # encontrar os elementos <span> que contenham os dados do produto
        for field in product_details:
            spans = field.find_all('span')
            product_dict[f'{spans[0].text.strip()[:-1]}'] = f'{spans[1].text}'

        # encontrar o elemento <img> que contenha a imagem do produto
        try:
            image_url = product_soup.find('img', id='og_image')['src']
        except TypeError:
            image_url = ''

        # criar ou atualizar um objeto Product com os dados obtidos
        product, created = models.Product.objects.update_or_create(
            code=product_dict['Code'],
            defaults={
                'barcode': product_dict['Bar Code'],
                'status': 'imported',
                'imported_t': timezone.now(),
                'url': product_url,
                'product_name': product_dict['Product Name'],
                'quantity': product_dict.get('Quantity', 'not found'),
                'categories': product_dict.get('Categories', 'not found'),
                'packaging': product_dict.get('Packaging', 'not found'),
                'brands': product_dict.get('Brands', 'not found'),
                'image_url': image_url,
            }
        )

        # imprimir uma mensagem informando se o produto foi criado ou atualizado
        if created:
            print(f'Product {product_dict["Product Name"]} created')
        else:
            print(f'Product {product_dict["Product Name"]} updated')

