# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-13 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0019_auto_20200913_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='weapon',
        ),
        migrations.AddField(
            model_name='heroweapon',
            name='hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='weapon', to='heroes.Hero'),
        ),
    ]
