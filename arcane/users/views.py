from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

# Create Playlist Tracks
class PlaylistTracks(View):
    def get(self, request, parent_lookup_playlist_tracks=-1):
        playlist = Playlist.objects.get(id=playlist_id)
        if playlist:
            tracks = playlist.tracks.all()
        else:
            tracks = []
        data = {
            'tracks': tracks
        }
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
