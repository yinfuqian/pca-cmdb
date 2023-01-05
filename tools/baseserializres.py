from rest_framework import serializers
from tools.basemodels import BaseModel
import time

class BaseSerializer(serializers.ModelSerializer):
    """基类序列化器"""
    create_tm_format = serializers.DateTimeField(source="created_tm",
                                                 format="%Y-%m-%d %H:%M:%S",
                                                 required=False,
                                                 read_only=True,
                                                 help_text='创建时间(北京时间)')

    update_tm_format = serializers.DateTimeField(source="updated_tm",
                                                 format="%Y-%m-%d %H:%M:%S",
                                                 required=False,
                                                 read_only=True,
                                                 help_text='更新时间(北京时间)')

    created_tm = serializers.DateTimeField(required=False,
                                           read_only=True,
                                           help_text='创建时间(时间戳)')

    updated_tm = serializers.DateTimeField(required=False,
                                           read_only=True,
                                           help_text='更新时间(时间戳)')

    class Meta:
        model = BaseModel
        fields = ("created_tm", "updated_tm",
                  "create_tm_format", "update_tm_format")
