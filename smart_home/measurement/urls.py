from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('sensors', views.SensorViewSet)
router.register('measurements', views.MeasurementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # path('sensors/', views.SensorViewSet.as_view()),
    # path('sensors/<int:pk>/', views.SensorDetail.as_view()),
    # path('measurements/', views.MeasurementViewSet.as_view()), 
]
