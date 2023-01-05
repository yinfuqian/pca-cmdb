from rest_framework import serializers
from tools.basemodels import BaseModel
from .models import Account
from tools.baseserializres import BaseSerializer
import time
"""
用户序列化"""

class UserSerializer(BaseSerializer):
    """用户基本信息"""
    id = serializers.IntegerField(read_only=True)

    class Meta:

        model = Account

        fields = ('username', 'password', 'id')

