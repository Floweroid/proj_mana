# Generated by Django 4.2.7 on 2024-05-26 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0010_alter_todo_created_at_alter_todo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Birthdate'),
        ),
    ]
