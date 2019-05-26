# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimesStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Cheff(TimesStampedModel):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)


class Recipe(TimesStampedModel):
    cheff_name = models.ForeignKey(Cheff, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=50)
    ingeridents = models.CharField(max_length=100)
    process = models.TextField()
