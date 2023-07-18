from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from main.models import Product, Blog


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


# class HomeListView(ListView):
#     model = Product
#     template_name = 'main/home.html'

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')                           # Эту функцию не перевести в cbv, так как она
        message = request.POST.get('message')                       # отвечает за статичную информацию.
        print(f'{name} ({email}): {message}')

    content = {'title': 'Contacts'}

    return render(request, 'main/home.html', content)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'preview', 'date_of_creation', 'count_of_views',)
    success_url = reverse_lazy('main:index')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog