from celery import shared_task
from .models import House, Apartment, WaterMeter, Tariff


@shared_task
def calculate_utility_bill(house_id, month):
    house = House.objects.get(id=house_id)
    apartments = Apartment.objects.filter(house=house)

    total_bill = 0
    for apartment in apartments:
        water_meter = apartment.water_meters.filter(month=month).first()
        if water_meter:
            tariff = apartment.tariff
            bill = water_meter.readings * tariff.price_per_unit + apartment.area * tariff.price_per_area
            total_bill += bill

    return total_bill
