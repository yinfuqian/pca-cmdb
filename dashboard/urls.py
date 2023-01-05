# -*- coding: utf-8 -*-
# 云机器
from django.conf.urls import include
from django.urls import re_path
from .views import *
urlpatterns = [
    # re_path(r'^index', IndexView.as_view(), name='index'),
    re_path(r'^cloud_capitals', include('cloud_capitals.urls'))
]
