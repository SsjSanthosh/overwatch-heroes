# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-11 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0008_auto_20200911_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='abilites',
        ),
    ]