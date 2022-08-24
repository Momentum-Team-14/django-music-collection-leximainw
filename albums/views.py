from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    resolve_url,
)
from django.utils import timezone
from .forms import (
    AlbumForm,
    ArtistForm,
)
from .models import (
    Album,
    Artist,
    Profile,
)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
        return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


def album_list(request):
    albums = Album.objects.all()
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        favorites = profile.favorites.values_list('id', flat=True)
    else:
        favorites = []
    return render(request, 'albums/album_list.html', {
        'page_name': 'Album List',
        'albums': albums,
        'favorites': favorites,
    })


def album_details(request, pk=None):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_details.html', {
        'page_name': 'Album Details',
        'album': album,
        'back_url': resolve_url('Album list'),
        'back_text': f'Back to album list',
    })


def album_new(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            return redirect('Album details', pk=form.save().pk)
        else:
            return redirect('/')
    else:
        form = AlbumForm()
        return render(request, 'albums/edit_form.html', {
            'page_name': 'Create Album',
            'form': form,
            'button_text': 'Create',
            'back_url': resolve_url('Album list'),
            'back_text': f'Back to album list',
        })


def album_edit(request, pk=None):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album.title = form.cleaned_data['title']
            album.artist = form.cleaned_data['artist']
            album.release_date = form.cleaned_data['release_date']
            album.save()
            return redirect('Album details', pk=album.pk)
        else:
            return redirect('/')
    else:
        form = AlbumForm(initial={
            'title': album.title,
            'artist': album.artist,
            'release_date': album.release_date,
        })
        return render(request, 'albums/edit_form.html', {
            'page_name': 'Edit Album',
            'form': form,
            'button_text': 'Save',
            'back_url': resolve_url('Album details', pk=album.pk),
            'back_text': f'Back to {album.title}',
        })


def album_delete(request, pk=None):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        if request.POST['confirm'] == album.title:
            album.delete()
            return redirect('Album list')
        else:
            return redirect('Album details', pk=album.pk)
    else:
        return render(request, 'albums/delete_form.html', {
            'page_name': 'Delete Album',
            'confirm_text': album.title,
            'back_url': resolve_url('Album details', pk=album.pk),
            'back_text': f'Back to {album.title}',
        })


def album_favorite(request, pk=None):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    album = get_object_or_404(Album, pk=pk)
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if profile.favorites.filter(pk=pk).exists():
        profile.favorites.remove(album)
        data = {'favorited': False}
    else:
        profile.favorites.add(album)
        data = {'favorited': True}
    return JsonResponse(data)


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_list.html', {
        'page_name': 'Artist List',
        'artists': artists,
    })


def artist_details(request, pk=None):
    artist = get_object_or_404(Artist, pk=pk)
    albums = Album.objects.filter(artist=artist)
    return render(request, 'albums/artist_details.html', {
        'page_name': 'Artist Details',
        'artist': artist,
        'albums': albums,
        'back_url': resolve_url('Artist list'),
            'back_text': 'Back to artist list',
    })


def artist_new(request, pk=None):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            return redirect('Artist details', pk=form.save().pk)
        else:
            return redirect('/')
    else:
        form = ArtistForm()
        return render(request, 'albums/edit_form.html', {
            'page_name': 'Create Artist',
            'form': form,
            'button_text': 'Create',
            'back_url': resolve_url('Artist list'),
            'back_text': 'Back to artist list',
        })


def artist_edit(request, pk=None):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist.name = form.cleaned_data['name']
            artist.save()
            return redirect('Artist details', pk=artist.pk)
        else:
            return redirect('/')
    else:
        form = ArtistForm(initial={
            'name': artist.name
        })
        return render(request, 'albums/edit_form.html', {
            'page_name': 'Edit Artist',
            'form': form,
            'button_text': 'Save',
            'back_url': resolve_url('Artist details', pk=artist.pk),
            'back_text': f'Back to {artist.name}',
        })


def artist_delete(request, pk=None):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        if request.POST['confirm'] == artist.name:
            artist.delete()
            return redirect('Artist list')
        else:
            return redirect('Artist details', pk=artist.pk)
    else:
        return render(request, 'albums/delete_form.html', {
            'page_name': 'Delete Artist',
            'confirm_text': artist.name,
            'back_url': resolve_url('Artist details', pk=artist.pk),
            'back_text': f'Back to {artist.name}',
        })
