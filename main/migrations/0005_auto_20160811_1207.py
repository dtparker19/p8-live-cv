# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160810_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='resume',
            name='lastname',
            field=models.CharField(default='No name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='middleinitial',
            field=models.CharField(default='0', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='picture',
            field=models.ImageField(max_length=50, upload_to='images/'),
        ),
    ]
