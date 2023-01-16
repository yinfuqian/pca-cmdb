# -*- coding: utf-8 -*-
# @Time : 2023/1/16 12:42
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py

from django.urls import re_path, path
from . import views
from .views import MachineRooms

urlpatterns = [
    re_path('machine_room/list/', MachineRooms.as_view(), name='machine_rooms_List')
]