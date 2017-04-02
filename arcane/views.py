from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from arcane.users.models import Listener
from arcane.users.api import ListenerSerializer
from django.contrib.auth.models import User
from django.core import serializers

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        listener = Listener.objects.get(user=user.id)
        print(listener)
        return Response({'token': token.key, 'listener': listener.id})
