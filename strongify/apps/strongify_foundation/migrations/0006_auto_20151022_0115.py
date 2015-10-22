# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0005_auto_20151022_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='routine',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='routine_step',
        ),
        migrations.AddField(
            model_name='routine',
            name='program',
            field=models.ForeignKey(default='placeholder', to='strongify_foundation.Program'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routinestep',
            name='routine',
            field=models.ForeignKey(default='placeholder', to='strongify_foundation.Routine'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='routinestep',
            name='repetition_set',
        ),
        migrations.AddField(
            model_name='routinestep',
            name='repetition_set',
            field=models.ManyToManyField(to='strongify_foundation.RepetitionSet'),
        ),
    ]
