from django.shortcuts import (
    get_object_or_404,
    render,
)
from .models import (
    Album,
    Artist,
)


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_details(request, pk=None):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_details.html', {'album': album})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_list.html', {'artists': artists})


def artist_details(request, pk=None):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'albums/artist_details.html', {'artist': artist})
