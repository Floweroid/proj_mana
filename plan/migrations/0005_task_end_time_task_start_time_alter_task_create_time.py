# Generated by Django 4.2.5 on 2023-09-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_alter_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
