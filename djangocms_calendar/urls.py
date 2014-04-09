from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import EventViewSet


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls))
)
