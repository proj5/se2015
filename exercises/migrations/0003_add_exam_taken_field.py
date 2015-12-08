# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_update_exercises'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]
