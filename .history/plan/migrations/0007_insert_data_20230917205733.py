# Generated by author on 2023-09-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('InProgress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
