# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-09 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200806_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='short_description',
            field=models.TextField(default=''),
        ),
    ]
