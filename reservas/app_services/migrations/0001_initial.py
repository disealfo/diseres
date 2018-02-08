# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
