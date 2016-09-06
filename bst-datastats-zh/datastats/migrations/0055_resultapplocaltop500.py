# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-01 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastats', '0054_auto_20160801_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultAppLocalTop500',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_date', models.DateField(verbose_name='\u65e5\u671f')),
                ('package_name', models.CharField(blank=True, max_length=256)),
                ('dst_count', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('version', models.CharField(default='', max_length=32)),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]