from django.conf.urls import include
from django.urls import re_path
from .views import *
urlpatterns = [
    re_path('list', UserListView.as_view(), name='user_list'),
    #re_path('/edit/?(\d+)', UserEdit.as_view(), name='user_edit'),
    #re_path('/test/$', UserTest.as_view())
    re_path('list/create', UserAddView.as_view(), name='user_create'),
    re_path('delete', UserDeleteView.as_view(), name='user_delete'),
    re_path('update', UserUpdateView.as_view(), name='user_update'),
    re_path('status', UserStatus.as_view(), name='user_status'),
    re_path('ssh', SSHListView.as_view(), name='ssh_list'),
]