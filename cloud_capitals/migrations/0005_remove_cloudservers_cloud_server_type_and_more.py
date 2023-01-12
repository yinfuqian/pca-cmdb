# Generated by Django 4.1.3 on 2023-01-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_capitals', '0004_alter_cloudtype_table_cloudversiontypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloudservers',
            name='cloud_server_type',
        ),
        migrations.AddField(
            model_name='cloudservers',
            name='cloud_product_type',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='产品类型'),
        ),
        migrations.AlterField(
            model_name='cloudservers',
            name='cloud_server_status',
            field=models.CharField(choices=[('0', '下线'), ('1', '在线'), ('2', '关机')], default='1', max_length=2, verbose_name='运行状态'),
        ),
    ]
