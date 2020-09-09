# Generated by Django 3.0.4 on 2020-09-09 12:10

from django.db import migrations, models
import uuid


def gen_uuid(apps, schema_editor):
    participant = apps.get_model('accounts', 'Participant')
    for row in participant.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20200909_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ), migrations.RunPython(gen_uuid),
    ]
