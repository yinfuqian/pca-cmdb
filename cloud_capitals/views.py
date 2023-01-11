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
class CloudServersListView(View):
    def get(self, request):
        data = CloudServers.objects.all().order_by('pk')
        return render(request, 'cloud_servers_list.html', {'data': data})

# 服务器更多信息
class CloudServersListInfoView(View):
    def get(self, request):
        data = CloudServers.objects.all().order_by('pk')
        return render(request, 'cloud_server_info.html', {'data': data})

# 服务器创建
class CloudServersCreateView(View):
    def post(self, request):
        data = request.POST

# 服务器状态修改
class CloudServersStatusView(View):
    def get(self, request):
        data = request.GET
        res = {'status': 0}

        cloud = CloudServers.objects.get(id=data.get('id'))

        # 0
        status = cloud.cloud_server_status

        print(data.get('name'))

        if status == "0":
            new_status = "1"
        else:
            new_status = "0"
        try:
            cloud = CloudServers.objects.get(id=data.get('id'))
            cloud.cloud_server_status = new_status
            cloud.save()

        except Exception as e:
            print(e)
            res = {'status': 1}
        return JsonResponse(res)

# 服务器删除
class CloudServersDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudServers()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudServers.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)
# 服务器更新
class CloudServersUpdata(View):
    def get(self, request):
        data = request.GET
        return render(request, 'cloud_server_update.html', {'cloud_obj': CloudServers.objects.get(id=request.GET.get('id'))})
    #
    # def post(self, request):
    #     data = request.POST
    #     # print(data)
    #     # print(data.get("id"))
    #     res = {'status': 0, 'msg': '更新成功'}
    #     try:
    #         username = data.get('username')
    #         password = data.get('password')
    #         account = data.get('system')
    #         email = data.get('email')
    #         phone = data.get('phone')
    #         is_active = data.get('is_act')
    #         is_superuser = data.get('is_sup')
    #         # print(username, password, email, phone, is_active, is_superuser)
    #         Account.objects.filter(id=data.get("id")).update(username=username,  email=email, phone=phone, is_active=is_active, is_superuser=is_superuser, role=account)
    #
    #     except Exception as e:
    #         print(e)
    #         res = {'status': '1', 'msg': '更新失败'}
    #     return JsonResponse(res)