# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0016_auto_20200913_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='health',
            field=models.CharField(max_length=256),
        ),
    ]
