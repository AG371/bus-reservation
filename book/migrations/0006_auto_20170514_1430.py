# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 09:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20170511_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='ticket',
        ),
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='book.Seat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='What the hell dude', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(20)]),
        ),
    ]