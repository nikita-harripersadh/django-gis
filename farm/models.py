from django.db import models

class FarmLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()   # Latitude as float
    longitude = models.FloatField()  # Longitude as float

    def __str__(self):
        return self.name


class Crop(models.Model):
    CROP_CHOICES = [
        ('wheat', 'Wheat'),
        ('corn', 'Corn'),
        ('rice', 'Rice'),
    ]
    farm_location = models.ForeignKey('farm.FarmLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    crop_type = models.CharField(
        max_length=5,
        choices=CROP_CHOICES,
        default='wheat',  # Default value for existing rows
    )
    planting_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.crop_type})"


class IrrigationZone(models.Model):
    farm_location = models.ForeignKey(FarmLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    polygon_data = models.TextField()  # Can store coordinates as text (e.g., JSON/WKT)

    def __str__(self):
        return self.name
