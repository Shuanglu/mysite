# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shawn', '0009_blogdetail_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetail',
            name='num',
        ),
        migrations.RemoveField(
            model_name='blogdetail',
            name='title',
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='comment',
            field=models.TextField(),
        ),
    ]
