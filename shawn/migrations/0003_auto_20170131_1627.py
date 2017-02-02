# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shawn', '0002_auto_20170128_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=3000)),
                ('title', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=3000)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Num',
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shawn.Blog'),
        ),
    ]