from django import forms
from albums.models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            'title',
            'artist',
            'release_date',
        )

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = (
            'name',
        )
