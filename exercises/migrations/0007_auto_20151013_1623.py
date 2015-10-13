# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20151013_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 9, 23, 49, 985556, tzinfo=utc), verbose_name=b'published date'),
        ),
    ]
