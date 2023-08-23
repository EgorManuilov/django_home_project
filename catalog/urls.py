from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, contacts, product_add

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('great_prod/', product_add)
]