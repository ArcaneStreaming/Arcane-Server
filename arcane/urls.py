"""arcane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.views import generic
from .views import CustomObtainAuthToken, letsencrypt
 
favicon_view = RedirectView.as_view(url='/static/images/favicon.png', permanent=True)

urlpatterns = [
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('arcane.browse.urls')),
    url(r'^api/auth/', CustomObtainAuthToken.as_view()),
    url(r'^api/users/', include('arcane.users.urls')),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^app/', generic.TemplateView.as_view(template_name='app.html')),
    url(r'^$', generic.TemplateView.as_view(template_name='construction.html')),
    # url(r'^api/', include(routers.SharedAPIRootRouter.router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^.well-known/acme-challenge/Gh-8m2Pl14h5ICX-KtpnJeQkIbAFGSEH7iuowIDR9qE', letsencrypt, name='letsencrtypt')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
