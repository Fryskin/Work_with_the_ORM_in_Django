from django.urls import path

from main.apps import MainConfig
from main.views import index, home

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home')
]
