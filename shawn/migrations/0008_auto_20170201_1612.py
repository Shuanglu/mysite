# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shawn', '0007_auto_20170201_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetail',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blogdetail',
            name='title',
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
