# Generated by Django 4.2.5 on 2024-05-04 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('req_doc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='definition',
            name='alias',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='别名'),
        ),
    ]