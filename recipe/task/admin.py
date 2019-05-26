# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cheff, Recipe

# Register your models here.
admin.site.register(Cheff)
admin.site.register(Recipe)
