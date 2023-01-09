import datetime
import time
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import *
from django.shortcuts import render, HttpResponse
from django.http import request, JsonResponse


# Create your views here.
#  云类型列表
class CloudCapListView(View):

    def get(self, request):
        data = CloudType.objects.all().order_by('pk')
        return render(request, 'cloud_cap_list.html', {'data': data})


# 云类型创建
class CloudCapCreateView(TemplateView):
    template_name = 'cloud_cap_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = CloudType()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# 云类型更新

class CloudCapUpdataView(TemplateView):
    def get(self, request):
        data = request.GET
        return render(request, 'cloud_cap_update.html', {'cloud_obj': CloudType.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            CloudType.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                               updated_tm=datetime.datetime.now().strftime(
                                                                   '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# 云类型删除

class CloudCapDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudType()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudType.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)

# 服务器列表
class CloudServersListView(TemplateView):
    template_name = 'cloud_servers_list.html'
