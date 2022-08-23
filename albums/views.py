from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone
from .forms import AlbumForm
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


def album_new(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_at = timezone.now()
            album.save()
            return redirect('Album details', pk=album.pk)
        else:
            return redirect('/')
    else:
        form = AlbumForm()
        return render(request, 'albums/album_edit.html', {
            'form': form,
            'button_text': 'Create',
        })


def album_edit(request, pk=None):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album.title = form.title
            album.artist = form.artist
            album.release_date = form.release_date
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
        return render(request, 'albums/album_edit.html', {
            'form': form,
            'button_text': 'Save'
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
            'confirm_text': album.title
        })


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_list.html', {'artists': artists})


def artist_details(request, pk=None):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'albums/artist_details.html', {'artist': artist})
