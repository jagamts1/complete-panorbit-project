# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panorbit_user', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
