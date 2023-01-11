# -*- coding: utf-8 -*-
# @Time : 2023/1/11 15:18
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py


from django.conf.urls import include
from django.urls import re_path, path
from .views import *

urlpatterns = [
    re_path(r'project_groups/list/', BusProjectsGroupListView.as_view(), name='projects_groups_list'),
    re_path(r'project_groups/update/', BusProjectsGroupUpdateView.as_view(), name='projects_groups_update'),
    re_path(r'project_groups/delete/', BusProjectsGroupDeleteView.as_view(), name='projects_groups_delete'),
    re_path(r'project_groups/create/', BusProjectsGroupCreateView.as_view(), name='projects_groups_create'),

    re_path(r'cloudtype/list/', CloudTypeListView.as_view(), name='cloud_type_list'),
    re_path(r'cloudtype/update/', CloudTypeUpdateView.as_view(), name='cloud_type_update'),
    re_path(r'cloudtype/delete/', CloudTypeDeleteView.as_view(), name='cloud_type_delete'),
    re_path(r'cloudtype/create/', CloudTypeCreateView.as_view(), name='cloud_type_create'),

    re_path(r'products/list/', ProductTypeListView.as_view(), name='product_type_list'),
    re_path(r'products/update/', ProductTypeUpdateView.as_view(), name='product_type_update'),
    re_path(r'products/delete/', ProductTypeDeleteView.as_view(), name='product_type_delete'),
    re_path(r'products/create/', ProductTypeCreateView.as_view(), name='product_type_create'),

    re_path(r'project_env/list/', ProductEnvListView.as_view(), name='project_env_list'),
    re_path(r'project_env/update/', ProductEnvUpdateView.as_view(), name='project_env_update'),
    re_path(r'project_env/delete/', ProductEnvDeleteView.as_view(), name='project_env_delete'),
    re_path(r'project_env/create/', ProductEnvCreateView.as_view(), name='project_env_create'),
]
