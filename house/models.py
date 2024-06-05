from django.db import models


class House(models.Model):
    address = models.CharField(max_length=200)


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='apartments')
    area = models.FloatField()


class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='water_meters')
    readings = models.FloatField()
    month = models.DateField()


class Tariff(models.Model):
    price_per_unit = models.FloatField()
    price_per_area = models.FloatField()
