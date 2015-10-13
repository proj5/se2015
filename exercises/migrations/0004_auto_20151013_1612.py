# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20151013_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'published date', null=True),
        ),
    ]
