from django.shortcuts import render

from main.models import Product


def index(request):
    products_list = Product.objects.all()
    content = {'object_list': products_list,
               'title': 'Main'}

    return render(request, 'main/index.html', content)


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    content = {'title': 'Contacts'}

    return render(request, 'main/home.html', content)
