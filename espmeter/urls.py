from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from meter.views import HomeView
from meter.api.views import SensorViewSet, LogEntryViewSet


api_router = routers.DefaultRouter()
api_router.register(r'logs', LogEntryViewSet)
api_router.register(r'sensors', SensorViewSet)

urlpatterns = [
    url(r'^api/', include(api_router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view())
]
