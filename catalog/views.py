from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/material_list.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


def product_add(request):
    product_for_create = []
    if request.method == 'POST':
        product = {
            'name_prod': request.POST.get('name'),
            'description_prod': request.POST.get('description'),
            'category_prod': request.POST.get('category'),
            'price_prod': request.POST.get('price'),
            'data_create_prod': datetime.now(),
            'data_change_prod': datetime.now()
        }
        product_for_create.append(
            Product(**product)
        )
        Product.objects.bulk_create(product_for_create)

    return render(request, 'catalog/great_prod.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ProductForm
    success_url = reverse_lazy('catalog:index')