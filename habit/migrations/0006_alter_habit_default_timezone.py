# Generated by Django 4.2.7 on 2024-05-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_remove_sleep_default_timezone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='default_timezone',
            field=models.CharField(default='America/New_York', max_length=50, verbose_name='Default Timezone'),
        ),
    ]
