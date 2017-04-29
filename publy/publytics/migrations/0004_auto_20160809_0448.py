# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publytics', '0003_auto_20160724_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('volume', models.IntegerField(verbose_name='volume')),
                ('bpm', models.IntegerField(verbose_name='bpm')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='checkin',
            options={'ordering': ['-created_at']},
        ),
    ]