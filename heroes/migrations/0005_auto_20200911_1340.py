# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-11 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0004_auto_20200911_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='armour',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='favourite_quote',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='occupation',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='real_name',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='shield',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='ammo',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='falloff_range',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='headshot',
            field=models.TextField(default=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='max_range',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='movement_speed',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='rate_of_fire',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='heroweapon',
            name='spread',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
    ]
