# Generated by Django 3.0.4 on 2020-03-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200323_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='participant',
            name='school',
            field=models.CharField(max_length=200),
        ),
    ]
