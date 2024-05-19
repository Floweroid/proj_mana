# Generated by Django 4.2.5 on 2024-05-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.TextField(verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('已完成', '已完成'), ('进行中', '进行中'), ('未开始', '未开始')], max_length=10, verbose_name='状态')),
                ('description', models.TextField(verbose_name='描述')),
                ('priority', models.IntegerField(verbose_name='优先级')),
                ('definitions', models.ManyToManyField(related_name='requirements', to='plan.definition', verbose_name='相关定义')),
            ],
        ),
    ]
