"""refugees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from records.models import Record
admin.autodiscover()

from rest_framework import filters, routers, permissions, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record

# viewsets define view behavior
class RecordViewset(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name')
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'records', RecordViewset)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^o/', include('oauth2_provider.urls', namespace = 'oauth2_provider')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
)