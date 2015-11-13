# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('done_time', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exam', models.ForeignKey(to='exercises.Exam')),
                ('user', models.ForeignKey(to='users.UserAccount')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('done_time', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exam_record', models.ForeignKey(related_name='exercise_records', default=None, blank=True, to='records.ExamRecord', null=True)),
                ('exercise', models.ForeignKey(related_name='records', to='exercises.Exercise')),
                ('user', models.ForeignKey(related_name='exercise_records', to='users.UserAccount')),
            ],
        ),
    ]
