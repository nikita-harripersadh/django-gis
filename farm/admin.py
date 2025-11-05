from django.contrib import admin
from .models import FarmLocation, Crop, IrrigationZone

@admin.register(FarmLocation)
class FarmLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ('name',)

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'crop_type', 'farm_location', 'planting_date')
    list_filter = ('crop_type',)
    search_fields = ('name',)

@admin.register(IrrigationZone)
class IrrigationZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm_location')
    search_fields = ('name',)
