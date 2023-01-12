from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from dashboard.models import Account
from cloud_capitals.models import *
from dashboard.serializers import AccountModeleSerializer
from cloud_capitals.serializers import CloudModeleSerializer
from business.serializers import *


# Create your views here.


class APIUserList(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountModeleSerializer


class APICloudList(viewsets.ModelViewSet):
    queryset = CloudType.objects.all()
    serializer_class = CloudModeleSerializer


class APIProjectGroupList(viewsets.ModelViewSet):
    queryset = CloudProjectsType.objects.all()
    serializer_class = ProjectGroupModeleSerializer


class APIServerTypeList(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeModeleSerializer

class APIServerEnvTypeList(viewsets.ModelViewSet):
    queryset = CloudEnvType.objects.all()
    serializer_class = CloudEnvTypeModeleSerializer

class APICloudVersionList(viewsets.ModelViewSet):
    queryset = CloudVersionTypes.objects.all()
    serializer_class = CloudVersionModeleSerializer


