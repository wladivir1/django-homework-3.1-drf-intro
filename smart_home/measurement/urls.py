from django.urls import path

from . import views


urlpatterns = [
    path('sensors/', views.SensorViewSet.as_view()),
    path('sensors/<int:pk>/', views.SensorDetail.as_view()),
    path('measurements/', views.MeasurementCreate.as_view()), 
]
