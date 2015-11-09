# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='exercises',
        ),
        migrations.AddField(
            model_name='exercise',
            name='skill',
            field=models.ForeignKey(related_name='exercises', default=None, blank=True, to='exercises.Skill', null=True),
        ),
    ]
