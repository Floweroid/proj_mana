# Generated by Django 4.2.7 on 2024-06-23 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('note', '0009_alter_notepointer_from_note_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('lName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('mid', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('fName', models.CharField(max_length=100, verbose_name='First Name')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Start Time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='End Time')),
                ('due', models.DateTimeField(blank=True, null=True, verbose_name='Deadline')),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='SocialRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=10, verbose_name='Relationship')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_relationships', to='social.person', verbose_name='From Person')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_relationships', to='social.person', verbose_name='To Person')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(choices=[('Linkin', 'Linkin'), ('TelephoneNum', 'TelephoneNum'), ('Wechat', 'Wechat'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram')], max_length=50, verbose_name='Media')),
                ('account', models.CharField(max_length=100, verbose_name='Account')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_accounts', to='social.person', verbose_name='Person')),
            ],
        ),
    ]