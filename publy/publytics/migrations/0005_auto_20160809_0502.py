# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publytics', '0004_auto_20160809_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='bpm',
            field=models.FloatField(verbose_name='bpm'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='volume',
            field=models.FloatField(verbose_name='volume'),
        ),
    ]