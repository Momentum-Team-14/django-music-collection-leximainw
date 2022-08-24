from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list),
    path('albums/', views.album_list, name='Album list'),
    path('albums/new/', views.album_new, name='New album'),
    path('albums/<int:pk>/', views.album_details, name='Album details'),
    path('albums/<int:pk>/edit/', views.album_edit, name='Edit album'),
    path('albums/<int:pk>/delete/', views.album_delete, name='Delete album'),
    path('albums/<int:pk>/favorite/', views.album_favorite, name='Favorite album'),
    path('artists/', views.artist_list, name='Artist list'),
    path('artists/new/', views.artist_new, name='New artist'),
    path('artists/<int:pk>/', views.artist_details, name='Artist details'),
    path('artists/<int:pk>/edit/', views.artist_edit, name='Edit artist'),
    path('artists/<int:pk>/delete/', views.artist_delete, name='Delete artist'),
]
