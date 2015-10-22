# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strongify_foundation', '0007_auto_20151022_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='routinestep',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True),
        ),
        migrations.AlterUniqueTogether(
            name='routine',
            unique_together=set([('program', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='routinestep',
            unique_together=set([('repetition_set', 'exercise')]),
        ),
    ]
