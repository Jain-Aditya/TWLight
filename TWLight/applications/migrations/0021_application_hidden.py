# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0020_auto_20180607_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
