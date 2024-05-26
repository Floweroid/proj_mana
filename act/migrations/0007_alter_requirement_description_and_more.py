# Generated by Django 4.2.7 on 2024-05-26 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0006_alter_requirement_parents_alter_requirement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='requirementrelationship',
            name='from_requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_requirements', to='act.requirement', verbose_name='源需求'),
        ),
        migrations.AlterField(
            model_name='requirementrelationship',
            name='to_requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_requirements', to='act.requirement', verbose_name='衍生需求'),
        ),
    ]
