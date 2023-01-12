# -*- coding: utf-8 -*-
# @Time : 2023/1/11 10:31
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py

from django.urls import re_path, path
from . import views

urlpatterns = [
    path("userlist/", views.APIUserList.as_view({'get': 'list'})),
    path("cloudlist/", views.APICloudList.as_view({'get': 'list'})),
    path("project_group_list/", views.APIProjectGroupList.as_view({'get': 'list'})),
    path("cloud_server_type_list/", views.APIServerTypeList.as_view({'get': 'list'})),
    path("server_owner_group_list/", views.APIServerTypeList.as_view({'get': 'list'})),
    path("server_env_type_list/", views.APIServerEnvTypeList.as_view({'get': 'list'})),
    path("cloud_version_list/", views.APICloudVersionList.as_view({'get': 'list'})),

]
