# Generated by Django 4.1.3 on 2022-12-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_capitals', '0002_rename_create_time_cloudcapitals_created_tm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('created_tm', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_tm', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'project_number',
                'ordering': ['-id'],
            },
        ),
        migrations.RenameField(
            model_name='cloudcapitals',
            old_name='expiration_time',
            new_name='project_expiration_time',
        ),
        migrations.RenameField(
            model_name='cloudcapitals',
            old_name='status',
            new_name='project_status',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='Public_ip',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='daq',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='disk',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='project',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='ssh_ip',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='ssh_port',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='ssh_user',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='svc_addr',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='system_product',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='type',
        ),
        migrations.RemoveField(
            model_name='cloudcapitals',
            name='users',
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_city',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='地域'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_cloud_name',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='公有云实例名'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_cloud_ownship',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='云归属'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_cloud_type',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='公有云版本'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_cloudid',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='实例ID'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_cost_env',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='成本归属'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_cost_money',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='月成本'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_env_type',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='环境'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_login_type',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='登陆方式'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_mark_tmp',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='临时备注'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_name',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='项目名称'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_number',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='项目编号'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_owner',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='责任人'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_pub_ip',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='公网IP'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_region',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='项目区域'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_ssh_ip',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='内网SSH地址'),
        ),
        migrations.AddField(
            model_name='cloudcapitals',
            name='project_type',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='业务类型'),
        ),
        migrations.CreateModel(
            name='CloudType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('created_tm', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_tm', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'cloudtype',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
    ]
