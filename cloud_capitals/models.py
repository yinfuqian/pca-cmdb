from django.db import models

# Create your models here.
from tools.basemodels import BaseModel
from dashboard.models import *

"""
环境类型
Prod/POC/test/dev/sit
"""


class Enviroment(BaseModel):
    class Meta:
        db_table = 'environments'
        ordering = ['-id']
        unique_together = ['name']


"""
云类型
"""


class CloudType(BaseModel):
    class Meta:
        db_table = "cloudtype"
        ordering = ['-id']
        unique_together = ['name']


"""
项目类型
运维公共项目/AIBPO业务中心...
"""


class Projects(BaseModel):
    class Meta:
        db_table = 'projects'
        ordering = ['-id']
        unique_together = ['name']


"""
业务类型
新业务/软件业务
"""


class ServicesAddr(BaseModel):
    class Meta:
        db_table = 'svc_addr'
        ordering = ['-id']
        unique_together = ['name']


"""
云资源类型"""


class CloudCpType(BaseModel):
    class Meta:
        db_table = 'cloud_cp_type'
        ordering = ['-id']
        unique_together = ['name']


"""
产品类型"""


class ProductType(BaseModel):
    class Meta:
        db_table = 'product_type'
        ordering = ['-id']
        unique_together = ['name']
"""
项目编号"""


class  ProjectNumber(BaseModel):
    class Meta:
        db_table = 'project_number'
        ordering = ['-id']


"""
云服务器"""

class CloudCapitals(BaseModel):
    STATUS = (
        ('0', u'下线'),
        ('1', u'在线'),
    )

    project_type = models.CharField(default="", null=True, max_length=50, verbose_name="业务类型")
    project_cost_env = models.CharField(default="", null=True, max_length=50,verbose_name="成本归属")
    project_login_type = models.CharField(default="", null=True, max_length=50, verbose_name="登陆方式")
    project_cloud_ownship = models.CharField(default="", null=True,max_length=50, verbose_name="云归属")
    project_city = models.CharField(default="", null=True, max_length=50, verbose_name="地域")
    project_cloudid = models.CharField(default="", null=True, max_length=50, verbose_name="实例ID")
    project_ssh_ip = models.CharField(default="", null=True, max_length=50, verbose_name="内网SSH地址")
    project_pub_ip = models.CharField(default="", null=True, max_length=50, verbose_name="公网IP")
    project_owner = models.CharField(default="", null=True, max_length=50, verbose_name="责任人")
    project_env_type = models.CharField(default="", null=True, max_length=50, verbose_name="环境")
    project_cloud_type = models.CharField(default="", null=True, max_length=50, verbose_name="公有云版本")
    project_region = models.CharField(default="", null=True, max_length=50, verbose_name="项目区域")
    project_number = models.CharField(default="", null=True, max_length=50, verbose_name="项目编号")
    project_name = models.CharField(default="", null=True, max_length=50, verbose_name="项目名称")
    project_cost_money = models.CharField(default="", null=True, max_length=50, verbose_name="月成本")
    project_cloud_name = models.CharField(default="", null=True, max_length=50, verbose_name="公有云实例名")
    project_mark_tmp = models.CharField(default="", null=True, max_length=50, verbose_name="临时备注")
    project_status = models.CharField(default='1', max_length=2, choices=STATUS, verbose_name='运行状态')
    project_expiration_time = models.DateTimeField(null=True, verbose_name="过期时间")
    class Meta:
        ordering = ['-id']
