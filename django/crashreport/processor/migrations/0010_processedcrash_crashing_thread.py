# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0009_auto_20151222_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='processedcrash',
            name='crashing_thread',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
