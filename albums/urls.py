from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='Album list')
]