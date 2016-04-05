# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crashsubmit', '0002_auto_20151214_1050'),
        ('processor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(help_text='The vendor of the device', max_length=100)),
                ('device', models.CharField(help_text='The device ID', max_length=100)),
                ('driver', models.CharField(help_text='The driver version', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedCrash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(choices=[('linux', 'linux'), ('windows', 'windows'), ('osx', 'osx'), ('android', 'android'), ('ios', 'ios')], max_length=10)),
                ('backtrace', models.TextField(help_text='The real backtrace of the crash')),
                ('signature', models.CharField(help_text='The signature(method in frame 0)', max_length=100)),
                ('crash_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crashsubmit.UploadedCrash', to_field='crash_id')),
                ('graphic_device', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='processor.GraphicDevice')),
            ],
        ),
    ]
