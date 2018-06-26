# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Part(models.Model):
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name