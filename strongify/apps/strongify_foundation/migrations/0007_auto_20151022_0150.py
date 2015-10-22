# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0006_auto_20151022_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routinestep',
            name='repetition_set',
        ),
        migrations.AddField(
            model_name='routinestep',
            name='repetition_set',
            field=models.ForeignKey(default='placeholder', to='strongify_foundation.RepetitionSet'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='routinestep',
            name='routine',
        ),
        migrations.AddField(
            model_name='routinestep',
            name='routine',
            field=models.ManyToManyField(to='strongify_foundation.Routine'),
        ),
    ]
