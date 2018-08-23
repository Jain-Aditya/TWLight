# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20180713_1831'),
        ('resources', '0051_auto_20180815_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='An access code for this partner.', max_length=30)),
                ('granted', models.BooleanField(default=False)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accesscodes', to='users.Editor')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesscodes', to='resources.Partner')),
            ],
            options={
                'verbose_name': 'access code',
                'verbose_name_plural': 'access codes',
            },
        ),
    ]
