# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0018_auto_20200913_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroweapon',
            name='healing',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='damage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
