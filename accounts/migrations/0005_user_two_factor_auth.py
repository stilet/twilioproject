# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170315_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='two_factor_auth',
            field=models.BooleanField(default=False),
        ),
    ]