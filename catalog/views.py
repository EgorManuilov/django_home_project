from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(f'{name} ({phone}): {email}')
    return render(request, 'catalog/index.html')
