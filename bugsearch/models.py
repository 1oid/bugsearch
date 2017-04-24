from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IP(models.Model):
    ip_addr = models.CharField(max_length=100)
    time_data = models.DateTimeField('search time')

    def __str__(self):
        return self.ip_addr