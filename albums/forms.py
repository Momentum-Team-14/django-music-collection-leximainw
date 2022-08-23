from django import forms
from albums.models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            'title',
            'artist',
            'release_date',
        )
