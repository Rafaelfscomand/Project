# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-23 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duplotubo', '0003_auto_20170527_2158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agua',
        ),
        migrations.DeleteModel(
            name='Butano',
        ),
        migrations.DeleteModel(
            name='CO2',
        ),
        migrations.DeleteModel(
            name='Metano',
        ),
        migrations.DeleteModel(
            name='Pentano',
        ),
        migrations.DeleteModel(
            name='RC318',
        ),
    ]
