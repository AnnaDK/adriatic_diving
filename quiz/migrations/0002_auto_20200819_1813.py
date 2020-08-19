# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='option_four_count',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_one_count',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_three_count',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_two_count',
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_four_checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_one_checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_three_checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_two_checkbox',
            field=models.BooleanField(default=False),
        ),
    ]
