# Generated by Django 4.2.7 on 2024-06-22 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_alter_note_related'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NoteMark',
            new_name='NotePointer',
        ),
    ]
