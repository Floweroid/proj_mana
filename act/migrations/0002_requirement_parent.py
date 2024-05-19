# Generated by Django 4.2.7 on 2024-05-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_requirements', to='act.requirement', verbose_name='父需求'),
        ),
    ]
