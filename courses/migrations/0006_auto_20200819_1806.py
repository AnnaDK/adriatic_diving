# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200813_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='minimum_age',
            field=models.CharField(default='', max_length=100),
        ),
    ]