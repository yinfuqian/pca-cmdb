from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from dashboard.models import Account
from cloud_capitals.models import *
from dashboard.serializers import AccountModeleSerializer
from cloud_capitals.serializers import CloudModeleSerializer
# Create your views here.


class APIUserList(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountModeleSerializer

class APICloudList(viewsets.ModelViewSet):
    queryset = CloudType.objects.all()
    serializer_class = CloudModeleSerializer