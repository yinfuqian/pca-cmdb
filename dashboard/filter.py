from tools.basefilter import BaseFilter
import django_filters
from .models import  Account

class UserFilter(django_filters.rest_framework.FilterSet):
    """用户基本信息"""
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    created_start_tm = django_filters.DateTimeFromToRangeFilter(field_name='创建开始时间')
    created_end_tm = django_filters.DateTimeFromToRangeFilter(field_name='创建结束时间')

    class Meta:
        model = Account
        field = ('id', 'username', 'created_start_tm', 'created_end_tm')
