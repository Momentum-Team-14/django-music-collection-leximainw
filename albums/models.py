from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Artist(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Album)


def on_user_saved(sender, instance, **kwargs):
    profile, created = Profile.objects.get_or_create(user=instance)
    if created:
        profile.save()


post_save.connect(on_user_saved, sender=User)
