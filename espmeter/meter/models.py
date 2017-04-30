from __future__ import unicode_literals

import json

from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.channel import Group

from meter.consumers import LIVESTREAM


class Sensor(models.Model):
    """ A simple model for a Sensor representation. """
    SENSOR_TEMPERATURE, SENSOR_HUMIDITY = range(1, 3)

    SENSOR_TYPE_CHOICES = (
        (SENSOR_TEMPERATURE, _('Temperature')),
        (SENSOR_HUMIDITY, _('Humidity'))
    )

    user = models.ForeignKey(User, related_name='sensors')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    type = models.PositiveSmallIntegerField(choices=SENSOR_TYPE_CHOICES, default=SENSOR_TEMPERATURE)
    
    class Meta:
        verbose_name = _('Sensor')
        verbose_name_plural = _('Sensors')
    
    @property
    def last_log(self):
        # Get the latest log entry
        return self.logs.last()


class LogEntry(models.Model):
    """ Sensor Log Entry. """
    
    sensor = models.ForeignKey(Sensor, related_name='logs')
    value = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Sensor Log Entry')
        verbose_name_plural = _('Sensor Log Entries')
    
    
@receiver(post_save, sender=LogEntry)
def send_update(sender, instance, **kwargs):
    # Send broadcast message to our livestream
    Group(LIVESTREAM).send({
        'text': json.dumps({
            'sensor_id': instance.sensor.id,
            'sensor_type': instance.sensor.type,
            'value': instance.value
        })
    })