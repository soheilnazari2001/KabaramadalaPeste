# Generated by Django 3.0.4 on 2020-03-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kabaramadalapeste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TreasureRewardItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_type', models.CharField(choices=[('SK', 'sekke'), ('VIS', 'vision'), ('TXP', 'travel express'), ('CHP', 'challenge plus'), ('PRC', 'prophecy'), ('BLY', 'bully')], default='SK', max_length=3)),
                ('amount', models.IntegerField(default=0)),
                ('treasure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='kabaramadalapeste.Treasure')),
            ],
        ),
        migrations.CreateModel(
            name='TreasureKeyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_type', models.CharField(choices=[('K1', 'key 1'), ('K2', 'key 2'), ('K3', 'key 3')], default='K1', max_length=2)),
                ('amount', models.IntegerField(default=0)),
                ('treasure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keys', to='kabaramadalapeste.Treasure')),
            ],
        ),
    ]