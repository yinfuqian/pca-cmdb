from django.db import models

# Create your models here.
from tools.basemodels import BaseModel
from dashboard.models import *


#  业务类型

"""
环境类型
Prod/POC/test/dev/sit
"""


class CloudEnvType(BaseModel):
    class Meta:
        db_table = 'environments'
        ordering = ['-id']
        unique_together = ['name']


"""
云类型
"""


class CloudType(BaseModel):
    class Meta:
        db_table = "cloud_type_name"
        ordering = ['-id']
        unique_together = ['name']


"""
项目组类型
运维公共项目/AIBPO业务中心...
"""


class CloudProjectsType(BaseModel):
    class Meta:
        db_table = 'cloud_project_groups'
        ordering = ['-id']
        unique_together = ['name']
"""
公有云版本类型
POC/多客户..
"""
class CloudVersionTypes(BaseModel):
    class Meta:
        db_table = 'cloud_project_type'
        ordering = ['-id']
        unique_together = ['name']

"""
云平台类型
腾讯云/阿里云
"""


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


class ProjectNumber(BaseModel):
    class Meta:
        db_table = 'cloud_server_number'
        ordering = ['-id']


"""
云服务器"""


class CloudServers(BaseModel):
    STATUS = (
        ('0', u'下线'),
        ('1', u'在线'),
    )
    cloud_server_type = models.CharField(default="", null=True, max_length=50, verbose_name="业务类型")
    cloud_server_check = models.CharField(default='0', max_length=2, verbose_name='是否核对')
    cloud_server_cost_env = models.CharField(default="", null=True, max_length=50, verbose_name="成本归属")
    cloud_server_login_type = models.CharField(default="", null=True, max_length=50, verbose_name="登陆方式")
    cloud_server_cloud_ownship = models.CharField(default="", null=True, max_length=50, verbose_name="云归属")
    cloud_server_city = models.CharField(default="", null=True, max_length=50, verbose_name="地域")
    cloud_server_cloudid = models.CharField(default="", null=True, max_length=50, verbose_name="实例ID")
    cloud_server_ssh_ip = models.CharField(default="", null=True, max_length=50, verbose_name="内网SSH地址")
    cloud_server_pub_ip = models.CharField(default="", null=True, max_length=50, verbose_name="公网IP")
    cloud_server_owner = models.CharField(default="", null=True, max_length=50, verbose_name="责任人")
    cloud_server_env_type = models.CharField(default="", null=True, max_length=50, verbose_name="环境")
    cloud_server_cloud_type = models.CharField(default="", null=True, max_length=50, verbose_name="公有云版本")
    cloud_server_region = models.CharField(default="", null=True, max_length=50, verbose_name="项目区域")
    cloud_server_number = models.CharField(default="", null=True, max_length=50, verbose_name="项目编号")
    cloud_server_name = models.CharField(default="", null=True, max_length=50, verbose_name="项目名称")
    cloud_server_cost_money = models.CharField(default="", null=True, max_length=50, verbose_name="月成本")
    cloud_server_cloud_name = models.CharField(default="", null=True, max_length=50, verbose_name="公有云实例名")
    cloud_server_mark_tmp = models.CharField(default="", null=True, max_length=50, verbose_name="临时备注")
    cloud_server_status = models.CharField(default='1', max_length=2, choices=STATUS, verbose_name='运行状态')
    cloud_server_expiration_time = models.DateTimeField(null=True, max_length=500, verbose_name="过期时间")
    cloud_server_cpus = models.CharField(default='', null=True, max_length=500, verbose_name='cpu')
    cloud_server_cpus_car = models.CharField(default='', null=True,max_length=500, verbose_name='cpu卡数')
    cloud_server_mems = models.CharField(default='', null=True,max_length=500, verbose_name='内存')
    cloud_server_sysdisks = models.CharField(default='', null=True,max_length=500, verbose_name='系统盘')
    cloud_server_datadisks = models.CharField(default='', null=True,max_length=500, verbose_name='数据盘')


    class Meta:
        ordering = ['id']
