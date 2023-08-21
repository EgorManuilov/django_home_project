from django.shortcuts import render

from catalog.models import Category


def home(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request, 'catalog/contacts.html', context)

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(name, phone, message)
#     return render(request, 'catalog/contacts.html')



