# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('possible_answer', models.CharField(max_length=200)),
                ('is_correct_answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='num_exercises',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='exam',
            name='time_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/img/', blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question_type',
            field=models.CharField(default=b'AN', max_length=2, choices=[(b'MC', b'multiple_choice'), (b'SC', b'single_choice'), (b'AN', b'answer')]),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='question',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='grade',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='possibleanswer',
            name='exercise',
            field=models.ForeignKey(related_name='possible', default=None, blank=True, to='exercises.Exercise', null=True),
        ),
    ]
