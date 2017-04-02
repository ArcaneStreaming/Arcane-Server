from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import os

from arcane import settings
from arcane.browse.models import Track, Artist

class Settings(models.Model):
    ARCANE_DARK = 'DARK'
    ARCANE_LIGHT = 'LIGH'
    PANDORA = 'PAND'
    SPOTIFY = 'SPOT'
    GOOGLE_PLAY = 'PLAY'
    CUSTOM = 'CUST'
    THEME_CHOICES = (
        (ARCANE_DARK, 'ARCANE_DARK'),
        (ARCANE_LIGHT, 'ARCANE_LIGHT'),
        (PANDORA, 'PANDORA'),
        (SPOTIFY, 'SPOTIFY'),
        (GOOGLE_PLAY, 'GOOGLE_PLAY'),
        (CUSTOM, 'CUSTOM'),
    )
    RIGHT = 'RIGH'
    LEFT = 'LEFT'
    HEADER = 'HEAD'
    FOOTER = 'FOOT'
    PLAYER_POSITION_CHOICES = (
        (RIGHT, 'RIGHT DRAWER'),
        (LEFT, 'LEFT DRAWER'),
        (HEADER, 'HEADER'),
        (FOOTER, 'FOOTER'),
    )
    theme = models.CharField(max_length=4, choices=THEME_CHOICES, default=ARCANE_DARK)
    player_pos = models.CharField(max_length=4, choices=PLAYER_POSITION_CHOICES, default=RIGHT)
    allow_explicit = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %r' % (self.theme, self.player_pos, self.allow_explicit)
    def __unicode__(self):
        return '%d: %s' % (self.id, self.__str__())


def upload_user_avatar(instance, file):
    name, extension = os.path.splitext(file)
    print(extension)
    # subpath = "avatar" + extension
    # path = os.path.join(settings.MEDIA_ROOT, "users", slugify(instance.id), subpath)
    # default_storage.save(path, ContentFile)
    return "users/" + slugify(instance.id) + "/avatar" + extension

class Listener(models.Model):
    # name = models.CharField(max_length=124)
    # email = models.EmailField()
    user = models.OneToOneField(User, related_name='listener', on_delete=models.CASCADE)
    location = models.CharField(max_length=3, default='USA')
    avatar = models.ImageField(upload_to=upload_user_avatar, blank=True, null=True)
    artist = models.ForeignKey(Artist, blank=True, null=True)
    settings = models.ForeignKey(Settings, blank=False, null=False, default=1)

    def __str__(self):
        # userFirst = User.objects.get(id=self.user)
        print('user:', self.location, self.user, self.user.first_name)
        return self.user.first_name + " " + self.user.last_name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)


# class Login(models.Model):
#     username = models.CharField(max_length=124)
#     password = models.CharField(max_length=124)
#     user = models.ForeignKey(User, blank=False, null=False)
#
#     def __str__(self):
#         return self.username
#
#     def __unicode__(self):
#         return '%d: %s' % (self.id, self.name)



class Playlist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Listener, blank=False, null=False)
    tracks = models.ManyToManyField(Track, symmetrical=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)
