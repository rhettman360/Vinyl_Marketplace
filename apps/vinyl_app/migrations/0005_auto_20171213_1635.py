# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 00:35
from __future__ import unicode_literals

import apps.vinyl_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl_app', '0004_auto_20171213_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinyl',
            name='picture',
            field=models.FileField(upload_to=apps.vinyl_app.models.path_and_rename),
        ),
    ]
