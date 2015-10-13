# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20151013_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 9, 13, 39, 406432, tzinfo=utc), null=True, verbose_name=b'published date'),
        ),
    ]
