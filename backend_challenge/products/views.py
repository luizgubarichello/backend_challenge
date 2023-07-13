from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination

class HomeView(generics.GenericAPIView):
    def get(self, request):
        return Response({"message": "Backend Challenge 20201026"})

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
