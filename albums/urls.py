from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list),
    path('albums/', views.album_list, name='Album list'),
    path('albums/<int:pk>/', views.album_details, name='Album details'),
    path('artists/', views.artist_list, name='Artist list'),
    path('artists/<int:pk>/', views.artist_details, name='Artist details'),
]
