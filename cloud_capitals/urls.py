from django.conf.urls import include
from django.urls import re_path
from .views import *

urlpatterns = [
    # re_path(r'^index', IndexView.as_view(), name='index'),
    re_path(r'/$', CloudView.as_view(), name='cloud'),
    re_path(r'/cloud_create', CloudCreateView.as_view(), name='cloud_create')
]