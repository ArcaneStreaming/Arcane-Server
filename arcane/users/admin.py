from django.contrib import admin
from arcane.users.models import Settings, Listener, Playlist #, Login,
admin.site.register(Settings)
admin.site.register(Listener)
# admin.site.register(Login)
admin.site.register(Playlist)
# Register your models here.
