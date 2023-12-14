# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementAddSerializer
from .models import Sensor, Measurement


class SensorViewSet(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorSerializer 
    
    
class SensorDetail(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
              
class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer          