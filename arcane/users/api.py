from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets, filters, validators
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from json import dumps
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Settings, Listener, Playlist #, Login
from arcane.browse.api import TrackSerializer, ArtistSerializer
from arcane.browse.models import Artist, Track


class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'theme', 'player_pos', 'allow_explicit')

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)

    def perform_create(self, serializer):
        serializer.save()

class ListenerSerializer(serializers.HyperlinkedModelSerializer):
    settings = serializers.PrimaryKeyRelatedField(queryset=Settings.objects.all())
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Listener
        fields = ('id', 'user', 'location', 'avatar', 'artist', 'settings')

class ListenerViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'artist')
    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=124, validators=[validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    listener = ListenerSerializer(read_only=True)
    first_name = serializers.CharField(min_length=1)
    last_name = serializers.CharField(min_length=1)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        # if user:
        #     token = Token.objects.create(user=user.id)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'listener', 'first_name', 'last_name')

class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'email')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save()
            if user:
                listener = Listener(user=user)
                listener.save()
                # return Response(serializer.data, status=status.HTTP_201_CREATED)

# class LoginSerializer(serializers.HyperlinkedModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     class Meta:
#         model = Login
#         fields = ('id', 'username', 'user', 'password')
#
# class LoginViewSet(viewsets.ModelViewSet):
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ('id', 'username', 'user')
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer
#     lookup_field = "id"
#
#     def perform_create(self, serializer):
#         serializer.save()

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(queryset=Track.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=Listener.objects.all())
    class Meta:
        model = Playlist
        fields = ('id', 'name', 'user', 'tracks')

class PlaylistViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_fields = ('id', 'user')
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()

    @detail_route(methods=['get'], url_path='tracks')
    def get_tracks(self, request, id=None):
        playlist = Playlist.objects.get(id=id)
        if playlist:
            tracks = list(map((lambda track: TrackSerializer(track).data), playlist.tracks.all()))
        else:
            tracks = []
        data = {'tracks': tracks}
        return HttpResponse(dumps(data), content_type='application/json')

def router_register(router):
    router.register(r'users', SettingsViewSet)
    router.register(r'users', UserViewSet)
    router.register(r'users', LoginViewSet)
    router.register(r'users', PlaylistViewSet)
