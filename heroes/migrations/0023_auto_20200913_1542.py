# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0022_auto_20200913_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroability',
            name='cooldown',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]