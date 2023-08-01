from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ContactView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
                        ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('home/', ContactView.as_view(), name='home'),
    path('create_product', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('view_product/<int:pk>/', ProductDetailView.as_view(), name='view_product')
]
