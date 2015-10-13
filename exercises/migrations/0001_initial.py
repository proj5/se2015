# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 10, 13, 12, 7, 30, 651673, tzinfo=utc), verbose_name=b'published date')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('num_skills', models.IntegerField(default=0)),
                ('num_exercises', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('num_exercises', models.IntegerField(default=0)),
                ('exercises', models.ManyToManyField(to='exercises.Exercise', blank=True)),
                ('grade', models.ForeignKey(related_name='skills', to='exercises.Grade')),
            ],
        ),
    ]
