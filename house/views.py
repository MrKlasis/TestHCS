from rest_framework import viewsets
from .models import House, Apartment, WaterMeter, Tariff
from .serializers import HouseSerializer, ApartmentSerializer, WaterMeterSerializer, TariffSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import calculate_utility_bill
from celery.result import AsyncResult


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer



@api_view(['POST'])
def start_calculation(request):
    house_id = request.data.get('house_id')
    month = request.data.get('month')
    task = calculate_utility_bill.delay(house_id, month)
    return Response({'task_id': task.id})


@api_view(['GET'])
def get_task_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        'task_id': task_id,
        'task_status': task_result.status,
        'task_result': task_result.result
    }
    return Response(result)
