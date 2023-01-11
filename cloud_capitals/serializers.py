# -*- coding: utf-8 -*-
# @Time : 2023/1/11 10:41
# @Author : yinfuqian
# @File : serializers.py
# @Project : manage.py

from rest_framework import serializers
from .models import CloudType


class CloudModeleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CloudType
        fields = ['name']

