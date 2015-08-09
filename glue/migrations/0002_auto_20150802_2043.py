# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('spawnIteration', models.IntegerField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='GameRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Mob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('hp', models.IntegerField()),
                ('location', models.ForeignKey(to='glue.Location')),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='MobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('startingHp', models.IntegerField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('currentLife', models.IntegerField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='PlayerConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('position', models.IntegerField()),
                ('mobEnd', models.ForeignKey(related_name='mobEnd', to='glue.Location')),
                ('mobSpawn', models.ForeignKey(related_name='mobSpawn', to='glue.Location')),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('maxQuantity', models.IntegerField()),
                ('spawnTimer', models.TimeField()),
                ('mobType', models.ForeignKey(to='glue.MobType')),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='config',
            field=models.ForeignKey(to='glue.PlayerConfig'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gameroom',
            name='users',
            field=models.ManyToManyField(to='glue.Player'),
        ),
        migrations.AddField(
            model_name='currentstage',
            name='mobs',
            field=models.ManyToManyField(to='glue.Mob'),
        ),
        migrations.AddField(
            model_name='currentstage',
            name='stage',
            field=models.ForeignKey(to='glue.Stage'),
        ),
    ]
