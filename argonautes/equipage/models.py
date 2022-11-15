from django.conf import settings
from django.db import models
from django.utils import timezone


class Crew_member(models.Model):

    name = models.CharField(verbose_name="", max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    belong_crew = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name