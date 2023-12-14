from rest_framework import serializers

from .models import Sensor, Measurement



class MeasurementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Measurement
        fields = [ 'temperature', 'created_at',  'image'] 
        
               
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        
 
class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = ['id','name', 'description']
        
    def create(self, validated_data):
        return super().create(validated_data)
 
        
class MeasurementAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'updated_at', 'image']
        
    def create(self, validated_data):
        return super().create(validated_data)                   