import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from cloud_capitals.models import *

# Create your views here.

"""
项目组相关
列表/创建/删除/更新
"""

class BusProjectsGroupListView(View):
    def get(self, request):
        data = CloudProjectsType.objects.all().order_by('pk')
        return render(request, 'business_group_list.html', {'data': data})

class BusProjectsGroupUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'business_group_update.html',
                      {'project_obj': CloudProjectsType.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            CloudProjectsType.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                       updated_tm=datetime.datetime.now().strftime(
                                                                           '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


class BusProjectsGroupDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudProjectsType()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudProjectsType.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


class BusProjectsGroupCreateView(TemplateView):
    template_name = 'business_group_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = CloudProjectsType()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


"""
公有云版本相关
列表/创建/删除/更新
"""


class CloudTypeListView(View):
    def get(self, request):
        data = CloudVersionTypes.objects.all().order_by('pk')
        return render(request, 'cloud_version_list.html', {'data': data})


class CloudTypeUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'cloud_version_update.html',
                      {'version_obj': CloudVersionTypes.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            CloudVersionTypes.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                       updated_tm=datetime.datetime.now().strftime(
                                                                           '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


class CloudTypeDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudVersionTypes()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudVersionTypes.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


class CloudTypeCreateView(TemplateView):
    template_name = 'cloud_version_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = CloudVersionTypes()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)

"""
产品类型
yibot/call 
"""
class ProductTypeListView(View):
    def get(self, request):
        data = ProductType.objects.all().order_by('pk')
        return render(request, 'product_type_list.html', {'data': data})


class ProductTypeUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'product_type_update.html',
                      {'product_type_obj': ProductType.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            ProductType.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                       updated_tm=datetime.datetime.now().strftime(
                                                                           '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


class ProductTypeDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = ProductType()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            ProductType.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


class ProductTypeCreateView(TemplateView):
    template_name = 'product_type_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = ProductType()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


"""
项目环境管理
"""


class ProductEnvListView(View):
    def get(self, request):
        data = CloudEnvType.objects.all().order_by('pk')
        return render(request, 'project_env_list.html', {'data': data})


class ProductEnvUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'project_env_update.html',
                      {'project_type_obj': CloudEnvType.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        print(data)
        try:
            name = data.get('name')
            remark = data.get('remark')
            CloudEnvType.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                 updated_tm=datetime.datetime.now().strftime(
                                                                     '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


class ProductEnvDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudEnvType()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudEnvType.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


class ProductEnvCreateView(TemplateView):
    template_name = 'project_env_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = CloudEnvType()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)
