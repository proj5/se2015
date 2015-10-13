# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20151013_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 16, 8, 43, 259982), null=True, verbose_name=b'published date'),
        ),
    ]
