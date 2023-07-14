from django.urls import path
from .views import HomeView, ProductDetailView, ProductListView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('products/<str:code>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
]
