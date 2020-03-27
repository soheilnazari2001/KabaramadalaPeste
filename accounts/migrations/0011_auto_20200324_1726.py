# Generated by Django 3.0.4 on 2020-03-24 12:56

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_merge_20200324_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='is_document_verified',
        ),
        migrations.AddField(
            model_name='participant',
            name='document_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Verified', 'Verified'), ('Rejected', 'Rejected')], default=accounts.models.ParticipantStatus['Pending'], max_length=30),
        ),
    ]