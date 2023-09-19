from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

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

    return render(request, 'catalog/product_add.html')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.object.user_boss = self.request.user
    #     self.object.save()
    #
    #     return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('object.title', 'avatar')
    success_url = reverse_lazy('catalog:product_add')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


def toggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('catalog:index'))
