# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20170503_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seating_pattern',
            field=models.CharField(choices=[('BUS_1', 'BUS_1'), ('BUS_2', 'BUS_2')], max_length=50),
        ),
    ]