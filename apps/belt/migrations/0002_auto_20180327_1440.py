# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(),
        ),
    ]
