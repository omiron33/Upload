# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0003_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='likers',
            field=models.ManyToManyField(related_name='favorites', to='belt.User'),
        ),
    ]