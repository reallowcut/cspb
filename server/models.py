from django.db import models
from django.utils import timezone
from rest_framework import serializers


class Illumination(models.Model):
    level = models.IntegerField()
    illumination_class = models.IntegerField(db_column='class', default=0)
    created_at = models.DateTimeField(auto_now_add=True)



