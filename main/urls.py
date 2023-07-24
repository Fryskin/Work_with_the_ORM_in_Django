from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ContactView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('home/', ContactView.as_view(), name='home')
]
