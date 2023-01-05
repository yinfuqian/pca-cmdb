# Generated by Django 4.1.3 on 2022-12-08 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0002_alter_account_options_account_role_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesAddr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'svc_addr',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'projects',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'product_type',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Enviroment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'environments',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='CloudCpType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'cloud_cp_type',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='CloudCapitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
                ('ssh_ip', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='SSH IP地址/内网地址')),
                ('ssh_port', models.IntegerField(blank=True, default=22, max_length=5, null=True, verbose_name='SSH 端口')),
                ('Public_ip', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='公网ip')),
                ('cpu', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='磁盘大小')),
                ('system_product', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='服务器类型')),
                ('daq', models.TextField(blank=True, default='', null=True, verbose_name='数据采集')),
                ('status', models.CharField(choices=[('0', '下线'), ('1', '在线')], default='1', max_length=2, verbose_name='运行状态')),
                ('expiration_time', models.DateTimeField(null=True, verbose_name='过期时间')),
                ('product_type', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cloud_capitals.producttype', verbose_name='产品类型')),
                ('project', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cloud_capitals.projects', verbose_name='项目归属')),
                ('ssh_user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='dashboard.sshuser', verbose_name='SSH用户')),
                ('svc_addr', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cloud_capitals.servicesaddr', verbose_name='所属区域')),
                ('type', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cloud_capitals.cloudcptype', verbose_name='所属云类型')),
                ('users', models.ManyToManyField(blank=True, default='', null=True, to=settings.AUTH_USER_MODEL, verbose_name='责任人')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
