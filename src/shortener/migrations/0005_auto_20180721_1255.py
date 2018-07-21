# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-21 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20180715_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]