# Create your views here.
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, request, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from dashboard.models import Account, SshUser
from django.db import connection
"""
用户列表展示
"""


class UserTest(View):
    def get(self, request):
        for i in range(0, 100):
            user = Account()
            user.username = 'ceshi{}'.format(i)
            user.password = 'admin1234'
            user.email = 'test{}@test.com'.format(i)
            user.phone = '155155644{}'.format(i)
            user.is_active = '1'
            user.is_superuser = '0'
            user.save()

        return HttpResponse("添加测试数据")


# 用户显示
class UserListView(ListView):
    template_name = 'user_list.html'
    model = Account
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', '-id')

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['page_range'] = self.page_range(context['page_obj'], context['paginator'])
        # print(context)
        return context

    def page_range(self, page_obj, paginator):
        current_page = page_obj.number
        start = current_page - 2
        end = current_page + 3
        if start < 1:
            start = 1
        if end > paginator.num_pages:
            end = paginator.num_pages + 1
        current_pages_num = end - start
        if (end == paginator.num_pages + 1):
            start = start - (5 - current_pages_num)
        else:
            if current_pages_num < 5:
                end = end + (5 - current_pages_num)
        return range(start, end)

# 添加用户
class UserAddView(TemplateView):
    template_name = 'user_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            user = Account()
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.phone = data.get('phone')
            # if data.get('is_act') == "激活":
            #     user.is_active = True
            # else:
            #     user.is_active = False
            user.is_active = data.get('is_act')
            user.is_superuser = data.get('is_sup')
            user.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)

# 删除用户
class UserDeleteView(View):
    def get(self, request):
        data = request.GET
        user = Account()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            Account.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)

# 更新用户
class UserUpdateView(View):
   # template_name = 'user_create.html'

    def get(self, request):
        data = request.GET
        return render(request, 'user_edit.html', {'user_obj': Account.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        print(data)
        print(data.get("id"))
        res = {'status': 0, 'msg': '更新成功'}
        try:
            username = data.get('username')
            password = data.get('password')
            account = data.get('system')
            email = data.get('email')
            phone = data.get('phone')
            is_active = data.get('is_act')
            is_superuser = data.get('is_sup')
            # print(username, password, email, phone, is_active, is_superuser)
            Account.objects.filter(id=data.get("id")).update(username=username,  email=email, phone=phone, is_active=is_active, is_superuser=is_superuser, role=account)

        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)

# 状态更新
class UserStatus(View):
    def get(self, request):
        data = request.GET

        res = {'status': 0}

        user = Account.objects.get(id=data.get('id'))
        status = user.is_active

        if status == 0:
            newstatus = 1
        else:
            newstatus = 0
        try:
            user = Account.objects.get(id=data.get('id'))
            user.is_active = newstatus
            user.save()
        except Exception as e:
            print(e)
            res = {'status': 1}
        return JsonResponse(res)

# SSHListView
class SSHListView(ListView):
        template_name = 'ssh_user_list.html'
        model = SshUser
        ordering = 'id'
        paginate_by = 8  # 单页显示

        def get_ordering(self):
            return self.request.GET.get('ordering', 'id')
