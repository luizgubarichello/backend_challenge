import pytest
from django.urls import reverse
from rest_framework import status
from .models import Product

@pytest.mark.django_db
def test_index_view(client):
    # Obter a url do endpoint /
    url = reverse('index')
    # Fazer uma requisição GET para o endpoint
    response = client.get(url)
    # Verificar se a resposta tem o status 200
    assert response.status_code == status.HTTP_200_OK
    # Verificar se a resposta tem a mensagem esperada
    assert response.data == {"message": "Fullstack Challenge 20201026"}

@pytest.mark.django_db
def test_product_detail_view(client):
    # Criar um produto de exemplo no banco de dados
    product = Product.objects.create(
        code=1234567890,
        barcode='1234567890(EAN / EAN-13)',
        status='imported',
        imported_t='2020-02-07T16:00:00Z',
        url='https://world.openfoodfacts.org/product/1234567890',
        product_name='Test product',
        quantity='100 g',
        categories='Test category',
        packaging='Test packaging',
        brands='Test brand',
        image_url='https://static.openfoodfacts.org/images/products/123/456/789/0/front_fr.3.400.jpg'
    )
    # Obter a url do endpoint /products/:code/
    url = reverse('product_detail', kwargs={'code': product.code})
    # Fazer uma requisição GET para o endpoint
    response = client.get(url)
    # Verificar se a resposta tem o status 200
    assert response.status_code == status.HTTP_200_OK
    # Verificar se a resposta tem os dados do produto esperados
    assert response.data == {
        'code': product.code,
        'barcode': product.barcode,
        'status': product.status,
        'imported_t': product.imported_t,
        'url': product.url,
        'product_name': product.product_name,
        'quantity': product.quantity,
        'categories': product.categories,
        'packaging': product.packaging,
        'brands': product.brands,
        'image_url': product.image_url
    }

@pytest.mark.django_db
def test_product_list_view(client):
    # Criar dois produtos de exemplo no banco de dados
    product1 = Product.objects.create(
        code=1234567890,
        barcode='1234567890(EAN / EAN-13)',
        status='imported',
        imported_t='2020-02-07T16:00:00Z',
        url='https://world.openfoodfacts.org/product/1234567890',
        product_name='Test product 1',
        quantity='100 g',
        categories='Test category 1',
        packaging='Test packaging 1',
        brands='Test brand 1',
        image_url='https://static.openfoodfacts.org/images/products/123/456/789/0/front_fr.3.400.jpg'
    )
    product2 = Product.objects.create(
        code=987654321,
        barcode='987654321(EAN / EAN-13)',
        status='imported',
        imported_t='2020-02-07T16:00:00Z',
        url='https://world.openfoodfacts.org/product/0987654321',
        product_name='Test product 2',
        quantity='200 g',
        categories='Test category 2',
        packaging='Test packaging 2',
        brands='Test brand 2',
        image_url='https://static.openfoodfacts.org/images/products/098/765/432/1/front_fr.3.400.jpg'
    )
    # Obter a url do endpoint /products/
    url = reverse('product_list')
    # Fazer uma requisição GET para o endpoint
    response = client.get(url)
    # Verificar se a resposta tem o status 200
    assert response.status_code == status.HTTP_200_OK
    # Verificar se a resposta tem a lista de produtos esperada
    assert response.data['results'] == [
        {
            'code': product1.code,
            'barcode': product1.barcode,
            'status': product1.status,
            'imported_t': product1.imported_t,
            'url': product1.url,
            'product_name': product1.product_name,
            'quantity': product1.quantity,
            'categories': product1.categories,
            'packaging': product1.packaging,
            'brands': product1.brands,
            'image_url': product1.image_url
        },
        {
            'code': product2.code,
            'barcode': product2.barcode,
            'status': product2.status,
            'imported_t': product2.imported_t,
            'url': product2.url,
            'product_name': product2.product_name,
            'quantity': product2.quantity,
            'categories': product2.categories,
            'packaging': product2.packaging,
            'brands': product2.brands,
            'image_url': product2.image_url
        }
    ]
