# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0025_heroability_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroability',
            name='health',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]