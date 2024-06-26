# Generated by Django 4.2.7 on 2024-05-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='笔记名称')),
                ('description', models.TextField(verbose_name='笔记')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('status', models.CharField(choices=[('已取消', '已取消'), ('已完成', '已完成'), ('进行中', '进行中'), ('未开始', '未开始')], default='未开始', max_length=10, verbose_name='状态')),
                ('description', models.TextField(verbose_name='描述')),
                ('priority', models.IntegerField(default=0, verbose_name='优先级')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
