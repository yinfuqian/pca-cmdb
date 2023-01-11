# -*- coding: utf-8 -*-
# @Time : 2023/1/11 10:31
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py

from django.urls import re_path, path
from . import views

urlpatterns = [
    path("userlist/", views.APIUserList.as_view({'get': 'list'})),
    path("cloudlist/", views.APICloudList.as_view({'get': 'list'}))
]


