# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastats', '0008_resultretention'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultretention',
            name='retention',
            field=models.CharField(default='1', max_length=10),
        ),
    ]