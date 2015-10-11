# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0001_squashed_0004_auto_20151011_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='type',
            new_name='movement_type',
        ),
    ]
