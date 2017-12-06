# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from json import dumps
from django.urls import reverse
from django.views import View
from django.db.models import Q
from django.db import models
from rest_framework import serializers, generics

from itertools import chain

from arcane.browse.models import Track, Artist, Album, Genre
from arcane.browse.api import TrackSerializer, ArtistSerializer, AlbumSerializer, GenreSerializer
from arcane.browse.forms import UploadForm

class List(View):
    def post(self, request):
    # Handle file upload
        form = UploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('uploadfiles')
        if form.is_valid():
            for f in files:
                Track.objects.create(url=f)
            # Redirect to the track list after POST
        return HttpResponseRedirect(reverse('list'))
    def get(self, request):
        form = UploadForm()  # A empty, unbound form

        # Load documents for the list page
        tracks = Track.objects.all()
        albums = Album.objects.all()
        artists = Artist.objects.all()
        genres = Genre.objects.all()

        # Render list page with the documents and the form
        return render(
            request,
            'list.html',
            {'tracks': tracks,
             'albums': albums,
             'artists': artists,
             'genres': genres,
             'form': form}
        )

class Upload(View):
    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('uploadfiles')
        explicitArr = request.FILES.getlist('isExplicit');
        filenames = request.POST.getlist('filenames')
        album_artwork = request.FILES.get('albumArtwork')
        album_name = request.POST.get('albumName')
        artist = request.POST.get('artist')
        album_genre = request.POST.get('albumGenre')
        print(artist)
        print(album_genre)
        print(album_name)
        print(album_artwork)
        print(filenames)
        print('Filenames length: ', len(filenames))

        newTracks = []
        print(files)
        print('Files length: ', len(files))

        if form.is_valid() and len(filenames) == len(files):
            artist = Artist.objects.get(pk=artist)
            genre = Genre.objects.get(pk=album_genre)
            newAlbum = Album.objects.create(name=album_name, artwork=album_artwork, genre=genre, artist=artist)
            for file, name, explicit in zip(files, filenames, explicitArr):
                newTracks.append(Track.objects.create(url=file, name=name, explicit=explicit, album=newAlbum, genre=genre, artist=artist))
        else:
            print("Filenames are not the same length as files")
            return HttpResponse('Malformed request: filenames provided is of different length than files provided', status=400)

        newTracks = list(map((lambda track: TrackSerializer(track).data), newTracks))
        data = {'tracks': newTracks}
        return HttpResponse(dumps(data), content_type='application/json')
        # Redirect to the track list after POST
        # return HttpResponseRedirect(reverse('upload'))

    def get(self, request):
        form = UploadForm()  # A empty, unbound form
        tracks=Track.objects.all()
        # Render list page with the documents and the form
        return render(
            request,
            'upload.html',
            {'tracks': tracks}
        )

class SearchModel(models.Model):
    name = models.CharField(max_length = 124)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchModel
        fields = ('id', 'name')

    def to_native(self, obj):
        print("serizlizing ", obj)
        if isinstance(obj, Track):
            serializer = TrackSerializer(obj)
        elif isinstance(obj, Artist):
            serializer = ArtistSerializer(obj)
        elif isinstance(obj, Album):
            serializer = AlbumSerializer(obj)
        elif isinstance(obj, Genre):
            serializer = GenreSerializer(obj)
        else:
            raise Exception("Neither a Snippet nor User instance!")
        return serializer.data


class Search(generics.ListAPIView):
    serializer_class = SearchSerializer

    def get_queryset(self):
        result = {}
        query = self.request.query_params.get('query', None)
        result['status'] = 'SUCCESS'
        tracks = Track.objects.filter(Q(name__icontains=query))
        albums = Album.objects.filter(Q(name__icontains=query))
        artists = Artist.objects.filter(Q(name__icontains=query))
        genres = Genre.objects.filter(Q(name__icontains=query))
        return list(chain(tracks, albums, artists, genres))
