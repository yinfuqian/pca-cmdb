# Generated by Django 4.1.3 on 2023-01-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_capitals', '0006_cloudservers_cloud_server_project_env'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudservers',
            name='cloud_server_cloud_name',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='公有云实例名'),
        ),
    ]
