from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomeView.as_view()),
    path('products/<str:code>/', views.ProductDetailView.as_view()),
    path('products/', views.ProductListView.as_view()),
]
