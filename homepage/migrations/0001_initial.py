# Generated by Django 3.0.4 on 2020-03-14 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countdown_date', models.DateTimeField(default=datetime.datetime(2020, 3, 23, 8, 0))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
