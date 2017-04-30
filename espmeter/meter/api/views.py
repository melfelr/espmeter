from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from meter.models import Sensor, LogEntry
from meter.api.serializers import SensorSerializer, LogEntrySerializer


class SensorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = SensorSerializer
    
    queryset = Sensor.objects.all()
    
    def get_queryset(self):
        qs = super(SensorViewSet, self).get_queryset()
        
        qs = qs.filter(
            user=self.request.user
        )
        
        return qs
    
    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user
        )
    
    @detail_route(methods=['get'], permission_classes=[AllowAny])
    def last_log(self, request, pk=None):
        sensor = self.get_object()
        
        serializer = LogEntrySerializer(sensor.last_log)
        
        return Response(serializer.data)

class LogEntryViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    
    serializer_class = LogEntrySerializer
    
    queryset = LogEntry.objects.all()
    
    def get_queryset(self):
        qs = super(LogEntryViewSet, self).get_queryset()
        
        qs = qs.filter(
            sensor__user=self.request.user
        )
        
        return qs
