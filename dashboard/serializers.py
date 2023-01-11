# -*- coding: utf-8 -*-
# @Time : 2023/1/11 10:41
# @Author : yinfuqian
# @File : serializers.py
# @Project : manage.py

from rest_framework import serializers
from .models import Account


class AccountModeleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username']

