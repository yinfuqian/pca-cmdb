from django.conf.urls import include
from django.urls import re_path, path
from .views import *

urlpatterns = [
    re_path(r'cloud/list', CloudCapListView.as_view(), name='cloud_cap_list'),
    re_path(r'cloud/create', CloudCapCreateView.as_view(), name='cloud_cap_create'),
    re_path(r'cloud/update', CloudCapUpdataView.as_view(), name='cloud_cap_update'),
    re_path(r'cloud/delete', CloudCapDeleteView.as_view(), name='cloud_cap_delete'),
    re_path(r'servers/list/info', CloudServersListInfoView.as_view(), name='cloud_servers_info'),
    re_path('servers/list/', CloudServersListView.as_view(), name='cloud_servers_list'),
    re_path('servers/create', CloudServersCreateView.as_view(), name='cloud_servers_create'),
    re_path('servers/status', CloudServersStatusView.as_view(), name='cloud_servers_status'),
    re_path('servers/delete', CloudServersDeleteView.as_view(), name='cloud_servers_delete'),
    re_path('servers/update', CloudServersUpdata.as_view(), name='cloud_servers_update'),

    
]
