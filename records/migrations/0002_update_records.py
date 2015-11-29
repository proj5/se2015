# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswerRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='exerciserecord',
            name='answer',
        ),
        migrations.AddField(
            model_name='useranswerrecord',
            name='exercise_record',
            field=models.ForeignKey(related_name='answer', default=None, blank=True, to='records.ExerciseRecord', null=True),
        ),
    ]
