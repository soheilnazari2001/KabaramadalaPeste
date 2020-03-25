# Generated by Django 3.0.4 on 2020-03-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200324_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='document_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Verified', 'Verified'), ('Rejected', 'Rejected')], default='Pending', max_length=30),
        ),
    ]
