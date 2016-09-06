# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-24 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluestacks', '0010_popwindow'),
    ]

    operations = [
        migrations.AddField(
            model_name='popwindow',
            name='button1_app_name',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='popwindow',
            name='button1_package_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popwindow',
            name='button2_app_name',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='popwindow',
            name='button2_package_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popwindow',
            name='button3_app_name',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='popwindow',
            name='button3_package_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]