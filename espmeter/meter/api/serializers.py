from rest_framework import serializers

from meter.models import Sensor, LogEntry


class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = (
            'id',
            'name',
            'description'
        )
        
class LogEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LogEntry
        fields = (
            'id',
            'sensor',
            'value'
        )
