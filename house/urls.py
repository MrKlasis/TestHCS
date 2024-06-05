from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseViewSet, ApartmentViewSet, WaterMeterViewSet, TariffViewSet, start_calculation, get_task_status

router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'water-meters', WaterMeterViewSet)
router.register(r'tariffs', TariffViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/start-calculation/', start_calculation),
    path('api/get-task-status/<str:task_id>/', get_task_status),
]
