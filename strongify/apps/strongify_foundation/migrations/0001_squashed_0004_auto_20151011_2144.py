# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    replaces = [('strongify_foundation', '0001_initial'), ('strongify_foundation', '0002_auto_20151011_2143'), ('strongify_foundation', '0003_exercise_type'), ('strongify_foundation', '0004_auto_20151011_2144')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100, choices=[('compound', 'Compound'), ('isolation', 'Isolation')])),
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
