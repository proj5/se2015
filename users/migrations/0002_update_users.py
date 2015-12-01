# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(default=b'static/img/default.jpg', upload_to=b'static/img/'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='facebook_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
