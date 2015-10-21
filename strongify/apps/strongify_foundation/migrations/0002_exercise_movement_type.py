# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='movement_type',
            field=models.CharField(choices=[('compound', 'Compound'), ('isolation', 'Isolation')], default='compound', max_length=100),
        ),
    ]
