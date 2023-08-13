from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import ProductListView, ContactView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
                        ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='index'),
    path('home/', ContactView.as_view(), name='home'),
    path('create_product', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('view_product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product')
]
