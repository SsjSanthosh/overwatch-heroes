# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0013_auto_20200913_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroultimate',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
