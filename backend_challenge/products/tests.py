from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_product_list(self):
        # Faz uma requisição GET real para a URL /products/
        response = self.client.get('/products/')
        # Verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
