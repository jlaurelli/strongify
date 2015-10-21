# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0002_exercise_movement_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='day_spread',
            field=models.PositiveIntegerField(choices=[(0, 'other'), (1, '1 Day'), (2, '2 Days'), (3, '3 Days'), (4, '4 Days'), (5, '5 Days'), (6, '6 Days'), (7, 'Everyday')], default=3),
        ),
    ]
