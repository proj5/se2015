# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20151013_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 12, 12, 42, 442200, tzinfo=utc), verbose_name=b'published date'),
        ),
        migrations.AddField(
            model_name='exam',
            name='exercises',
            field=models.ManyToManyField(to='exercises.Exercise', blank=True),
        ),
    ]
