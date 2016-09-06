# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-25 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datastats', '0045_auto_20160725_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midresultinstallinitemulator',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='midresultinstallinitengine',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultappactivity',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultappinstall',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultappsession',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultapptotal',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultemulatoractivity',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultemulatorinstall',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultemulatorinstallcount',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultemulatorsession',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultemulatoruninstallcount',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultemulatoruninstallnextdaycount',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultengineactivity',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultenginedau',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultengineinstall',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultengineuninstallrate',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultgeneralapkinsterror',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultgeneralengineinstall',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultgeneralengineinsterror',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultgeneralenginiterror',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultgeneralosversion',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultgeneraluninstallreason',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultretention',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultretentionengine',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultusercomputerinfocpu',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultusercomputerinfomemory',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='resultusercomputerinfoos',
            name='channel',
        ),
    ]