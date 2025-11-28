from django.db import models
from django.contrib.auth.models import User

# ------------------------
# BaseModel for shared fields
# ------------------------
class BaseModel(models.Model):
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        abstract = True  # Prevents table creation for BaseModel

# ------------------------
# Farm Models
# ------------------------
class FarmLocation(BaseModel):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()   # Latitude as float
    longitude = models.FloatField()  # Longitude as float

    def __str__(self):
        return self.name


class Crop(BaseModel):
    CROP_CHOICES = [
        ('wheat', 'Wheat'),
        ('corn', 'Corn'),
        ('rice', 'Rice'),
    ]
    farm_location = models.ForeignKey(FarmLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    crop_type = models.CharField(
        max_length=5,
        choices=CROP_CHOICES,
        default='wheat',  # Default value for existing rows
    )
    planting_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.crop_type})"


class IrrigationZone(BaseModel):
    farm_location = models.ForeignKey(FarmLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    polygon_data = models.TextField()  # Can store coordinates as text (e.g., JSON/WKT)

    def __str__(self):
        return self.name
