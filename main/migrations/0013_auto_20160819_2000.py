# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160816_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='word',
            field=models.CharField(max_length=50),
        ),
    ]