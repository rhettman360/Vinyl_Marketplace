# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl_app', '0003_vinyl_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinyl',
            name='picture',
            field=models.FileField(upload_to='apps/vinyl_app/static/images/'),
        ),
    ]