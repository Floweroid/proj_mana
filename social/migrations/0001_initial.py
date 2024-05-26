# Generated by Django 4.2.7 on 2024-05-26 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lName', models.CharField(max_length=100, verbose_name='姓氏')),
                ('mid', models.CharField(blank=True, max_length=100, null=True, verbose_name='中间名')),
                ('fName', models.CharField(max_length=100, verbose_name='名字')),
                ('hometown', models.CharField(blank=True, max_length=100, null=True, verbose_name='家乡')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='SocialRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=100, verbose_name='关系类型')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_relationships', to='social.person', verbose_name='从')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_relationships', to='social.person', verbose_name='到')),
            ],
        ),
    ]