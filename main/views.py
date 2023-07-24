from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView

from main.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'
    extra_context = {'title': 'Main Page'}


# class HomeListView(ListView):
#     model = Product
#     template_name = 'main/home.html'

class ContactView(TemplateView):
    template_name = 'main/home.html'
    extra_context = {
        'title': 'Contacts'
    }

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)




