# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onenote',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
    ]