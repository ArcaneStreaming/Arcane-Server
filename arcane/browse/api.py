from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, filters, pagination
from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import Genre, Artist, ArtistSummary, Album, Track

class TileResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ListResultsSetPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.StringRelatedField(many=True)
    class Meta:
        model = Genre
        fields = ('id', 'name', 'color', 'icon', 'artists')

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'id')
    ordering_fields = ('name','color')
    ordering = ('name')
    lookup_field = "id"
    pagination_class = TileResultsSetPagination

    def perform_create(self, serializer):
        serializer.save()


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # genre = GenreSerializer(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)
    albums = serializers.StringRelatedField(many=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre', 'cover_photo', 'albums')

class ArtistViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'id', 'genre')
    ordering_fields = ('name','genre')
    ordering = ('name')
    lookup_field = "id"
    pagination_class =TileResultsSetPagination

    def perform_create(self, serializer):
        serializer.save()


class ArtistSummarySerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    class Meta:
        model = ArtistSummary
        fields = ('id', 'artist', 'summary')


class ArtistSummaryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ArtistSummarySerializer
    queryset = ArtistSummary.objects.all().select_related('artist')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'artist')
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    # artist = ArtistSerializer(read_only=True)
    # genre = GenreSerializer(read_only=True)
    artist = serializers.StringRelatedField(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)
    tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ('id', 'name', 'artist', 'genre', 'artwork', 'tracks')

class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'id', 'artist', 'genre')
    ordering_fields = ('name','artist','genre','id')
    ordering = ('name',)
    lookup_field = "id"
    pagination_class =TileResultsSetPagination

    def perform_create(self, serializer):
        serializer.save()


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    artist = ArtistSerializer(read_only=True)
    # genre = GenreSerializer(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Track
        fields = ('id', 'order', 'name', 'duration', 'length', 'artist', 'album', 'genre', 'url', 'play_count')

class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter,)
    filter_fields = ('album', 'id', 'name', 'genre', 'artist')
    ordering_fields = ('order', 'name','album','artist','genre','id')
    ordering = ('name',)
    search_fields = ('name',)
    lookup_field = "id"
    pagination_class = ListResultsSetPagination

    # def filter_queryset(self, queryset):
    #     queryset = super(TrackViewSet, self).filter_queryset(queryset)
    #     return queryset.order_by('name')

    def perform_create(self, serializer):
        serializer.save()

def router_register(router):
    router.register(r'users', AlbumViewSet)
    router.register(r'users', ArtistViewSet)
    router.register(r'users', ArtistSummaryViewSet)
    router.register(r'users', GenreViewSet)
    router.register(r'users', TrackViewSet)
