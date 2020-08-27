# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-27 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(max_length=40),
        ),
    ]
