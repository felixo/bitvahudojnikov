# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bh2017', '0004_auto_20170312_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='jury',
            name='Post',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='jury',
            name='docfile',
            field=models.FileField(default='', upload_to='Jurys'),
        ),
        migrations.AddField(
            model_name='jury',
            name='text',
            field=models.CharField(default='', max_length=2000),
        ),
    ]