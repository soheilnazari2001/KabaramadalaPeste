# Generated by Django 3.0.4 on 2020-03-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_paymentattempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentattempt',
            name='red_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='paymentattempt',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
