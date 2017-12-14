# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'apps/vinyl_app/static/images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        # filename = '{}.{}'.format(uuid4().hex, ext)
        filename = 'test' + ext
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Vinyl(models.Model):
    title = models.TextField(max_length=255)
    artist = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.TextField(max_length=8)
    picture = models.FileField(upload_to=path_and_rename)
    created_at = models.DateTimeField(auto_now_add=True)
