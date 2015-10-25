# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('movement_type', models.CharField(choices=[('compound', 'Compound'), ('isolation', 'Isolation')], max_length=100, default='compound')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('day_spread', models.PositiveIntegerField(choices=[(0, 'other'), (1, '1 Day'), (2, '2 Days'), (3, '3 Days'), (4, '4 Days'), (5, '5 Days'), (6, '6 Days'), (7, 'Everyday')], default=3)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RepetitionSet',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('repetition_set', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=2)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('program', models.ForeignKey(to='strongify_foundation.Program')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineStep',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('exercise', models.ForeignKey(to='strongify_foundation.Exercise')),
                ('repetition_set', models.ForeignKey(to='strongify_foundation.RepetitionSet')),
                ('routine', models.ManyToManyField(to='strongify_foundation.Routine')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='routinestep',
            unique_together=set([('repetition_set', 'exercise')]),
        ),
        migrations.AlterUniqueTogether(
            name='routine',
            unique_together=set([('program', 'name')]),
        ),
    ]
