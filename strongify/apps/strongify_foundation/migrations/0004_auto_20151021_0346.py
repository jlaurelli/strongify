# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0003_program_day_spread'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepetitionSet',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('repetition_set', django.contrib.postgres.fields.ArrayField(size=None, base_field=django.contrib.postgres.fields.ArrayField(size=2, base_field=models.PositiveIntegerField()))),
            ],
        ),
        migrations.CreateModel(
            name='RoutineStep',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('exercise', models.ForeignKey(to='strongify_foundation.Exercise')),
                ('repetitions', models.ForeignKey(to='strongify_foundation.RepetitionSet')),
            ],
        ),
        migrations.RemoveField(
            model_name='routine',
            name='exercise',
        ),
        migrations.AddField(
            model_name='routine',
            name='routine_step',
            field=models.ManyToManyField(to='strongify_foundation.RoutineStep'),
        ),
    ]
