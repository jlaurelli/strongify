# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0004_auto_20151021_0346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routinestep',
            old_name='repetitions',
            new_name='repetition_set',
        ),
        migrations.AlterField(
            model_name='repetitionset',
            name='repetition_set',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=2),
        ),
    ]
