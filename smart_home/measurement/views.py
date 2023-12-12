# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
#from rest_framework import generics
from rest_framework.response import Response
#from rest_framework.views import APIView

from .serializers import SensorSerializer, MeasurementSerializer
from .models import Sensor, Measurement


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
       
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# class SensorViewSet(generics.ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer 
    
    
# class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
    
              
# class MeasurementViewSet(generics.ListCreateAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer          