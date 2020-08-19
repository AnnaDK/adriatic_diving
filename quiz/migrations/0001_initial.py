# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=200)),
                ('option_two', models.CharField(max_length=200)),
                ('option_three', models.CharField(max_length=200)),
                ('option_four', models.CharField(max_length=200)),
                ('option_one_count', models.BooleanField(default=True)),
                ('option_two_count', models.BooleanField(default=True)),
                ('option_three_count', models.BooleanField(default=True)),
                ('option_four_count', models.BooleanField(default=True)),
                ('answer', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
