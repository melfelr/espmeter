from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import ugettext as _


class Sensor(models.Model):
    """ A simple model for a Sensor representation. """
    user = models.ForeignKey(User, related_name='sensors')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _('Sensor')
        verbose_name_plural = _('Sensors')
    
    @property
    def last_log(self):
        # Get the latest log entry
        return self.logs.last()


class LogEntry(models.Model):
    """ Sensor Log Entry. """
    LOG_TEMPERATURE, LOG_HUMIDITY = range(1, 3)
    
    LOG_CHOICES = (
        (LOG_TEMPERATURE, _('Temperature')),
        (LOG_HUMIDITY, _('Humidity'))
    )
    
    sensor = models.ForeignKey(Sensor, related_name='logs')
    value = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Sensor Log Entry')
        verbose_name_plural = _('Sensor Log Entries')
    
    
