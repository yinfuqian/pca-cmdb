# -*- coding: utf-8 -*-
# @Time : 2023/1/16 12:42
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py

from django.urls import re_path, path
from . import views
from .views import *

urlpatterns = [
    re_path('machine_room/list/', MachineRoomsList.as_view(), name='machine_rooms_List'),
    re_path('machine_room/create/', MachineRoomsCreate.as_view(), name='machine_rooms_create'),
    re_path('machine_root/update/', MachineRoomsUpdate.as_view(), name='machine_rooms_update'),
    re_path('machine_root/delete/', MachineRoomsDelete.as_view(), name='machine_rooms_delete'),
    re_path('machine_cupb/list/', MachineCupbList.as_view(), name='machine_cupb_list'),
    re_path('machine_cupb/create/', MachineCupbCreate.as_view(), name='machine_cupb_create'),
    re_path('machine_cupb/update/', MachineCupbUpdate.as_view(), name='machine_cupb_update'),
    re_path('machine_cupb/delete/', MachineCupbDelete.as_view(), name='machine_cupb_delete'),
]