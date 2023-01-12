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
        return render(request, 'cloud_server_update.html',
                      {'cloud_obj': CloudServers.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        # print(data)
        # print(data.get("id"))
        res = {'status': 0, 'msg': '更新成功'}
        try:
            print(data)
            cloud_server_owner = data.get('username')
            cloud_server_cpus = data.get('cpus')
            cloud_server_mems = data.get('mem')
            cloud_server_cpus_car = data.get('cpu_cars')
            cloud_server_sysdisks = data.get('system_disk')
            cloud_server_datadisks = data.get('cloud_server_data_disks')
            cloud_server_check = data.get('is_check')
            cloud_server_login_type = data.get('ssh_method')
            cloud_product_type = data.get('cloud_product_type')

            cloud_server_status = data.get('cloud_server_status')
            cloud_server_cost_env = data.get('cloud_ownership_group')
            cloud_server_cloud_ownship = data.get('cloud_type')
            cloud_server_city = data.get('cloud_region_city')
            cloud_server_ssh_ip = data.get('ip_in')
            cloud_server_pub_ip = data.get('ip_out')
            cloud_server_env_type = data.get('cloud_env')
            cloud_server_cloud_type = data.get('cloud_version')
            cloud_server_region = data.get('cloud_porject_region')
            cloud_server_number = data.get('cloud_server_number')
            cloud_server_cost_money = data.get('cloud_server_cost_money')
            cloud_server_project_env = data.get('cloud_server_cost_env')
            cloud_server_mark_tmp = data.get('tmp_remark')
            remark = data.get('remark')

            # print(username, password, email, phone, is_active, is_superuser)
            # Account.objects.filter(id=data.get("id")).update(username=username,  email=email, phone=phone, is_active=is_active, is_superuser=is_superuser, role=account)
            CloudServers.objects.filter(id=data.get("id")).update(cloud_server_owner=cloud_server_owner,
                                                                  cloud_server_cpus=cloud_server_cpus,
                                                                  cloud_server_mems=cloud_server_mems,
                                                                  cloud_server_cpus_car=cloud_server_cpus_car,
                                                                  cloud_server_sysdisks=cloud_server_sysdisks,
                                                                  cloud_server_check=cloud_server_check,
                                                                  cloud_server_login_type=cloud_server_login_type,
                                                                  cloud_product_type=cloud_product_type,
                                                                  cloud_server_status=cloud_server_status,
                                                                  cloud_server_cost_env=cloud_server_cost_env,
                                                                  cloud_server_cloud_ownship=cloud_server_cloud_ownship,
                                                                  cloud_server_city=cloud_server_city,
                                                                  cloud_server_ssh_ip=cloud_server_ssh_ip,
                                                                  cloud_server_pub_ip=cloud_server_pub_ip,
                                                                  cloud_server_env_type=cloud_server_env_type,
                                                                  cloud_server_cloud_type=cloud_server_cloud_type,
                                                                  cloud_server_region=cloud_server_region,
                                                                  cloud_server_number=cloud_server_number,
                                                                  cloud_server_cost_money=cloud_server_cost_money,
                                                                  cloud_server_project_env=cloud_server_project_env,
                                                                  cloud_server_mark_tmp=cloud_server_mark_tmp,
                                                                  cloud_server_datadisks=cloud_server_datadisks,
                                                                  remark=data.get('remark'),
                                                                  updated_tm=datetime.datetime.now().strftime(
                                                                      '%Y-%m-%d %H:%M:%S.%f')
                                                                  )
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)
