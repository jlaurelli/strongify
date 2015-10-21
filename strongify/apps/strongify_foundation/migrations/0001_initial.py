# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='strongify_foundation.Exercise')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='routine',
            field=models.ManyToManyField(to='strongify_foundation.Routine'),
        ),
    ]