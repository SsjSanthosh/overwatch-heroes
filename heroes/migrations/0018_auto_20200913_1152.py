# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0017_auto_20200913_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]