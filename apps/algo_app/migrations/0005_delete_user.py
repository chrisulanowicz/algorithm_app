# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algo_app', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
