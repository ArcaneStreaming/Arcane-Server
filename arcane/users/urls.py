# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views, api
from django.views import generic

schema_view = get_schema_view(title="Arcane API")

router = DefaultRouter()
router.register(r'settings', api.SettingsViewSet)
router.register(r'users', api.UserViewSet, 'user')
router.register(r'listeners', api.ListenerViewSet)
# router.register(r'login', api.LoginViewSet)
router.register(r'playlists', api.PlaylistViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]
