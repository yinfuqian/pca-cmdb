# -*- coding: utf-8 -*-
# @Time : 2023/1/12 9:55
# @Author : yinfuqian
# @File : serializers.py
# @Project : manage.py
from rest_framework import serializers
from cloud_capitals.models import CloudProjectsType, ProductType, CloudVersionTypes


class ProjectGroupModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudProjectsType
        fields = "__all__"


class ProductTypeModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class CloudEnvTypeModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"

class CloudVersionModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudVersionTypes
        fields = "__all__"
