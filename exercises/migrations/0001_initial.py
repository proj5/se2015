# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
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
        migrations.AddField(
            model_name='exam',
            name='exercises',
            field=models.ManyToManyField(to='exercises.Exercise', blank=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='grade',
            field=models.ForeignKey(related_name='exams', to='exercises.Grade'),
        ),
    ]
