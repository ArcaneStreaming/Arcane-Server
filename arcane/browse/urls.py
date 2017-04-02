# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from arcane.browse.views import List, Upload, Search
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_extensions.routers import ExtendedSimpleRouter
from . import views, api
from django.views import generic

schema_view = get_schema_view(title="Arcane API")

router = ExtendedSimpleRouter()
(
router.register(r'artists', api.ArtistViewSet)
      .register(r'summary', api.ArtistSummaryViewSet, base_name='artist-summaries', parents_query_lookups=['summary__artist','artist'])
)
router.register(r'albums', api.AlbumViewSet)
router.register(r'genres', api.GenreViewSet)
router.register(r'tracks', api.TrackViewSet)

urlpatterns = [
    url(r'^list/$', List.as_view()),
    url(r'^upload/$', Upload.as_view()),
    url(r'^search/$', Search.as_view()),
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
]
