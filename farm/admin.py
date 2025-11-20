from django.contrib import admin
from .models import FarmLocation, Crop, IrrigationZone

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('last_update', 'last_update_by')

    def save_model(self, request, obj, form, change):
        obj.last_update_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(FarmLocation)
class FarmLocationAdmin(BaseAdmin):
    pass

@admin.register(Crop)
class CropAdmin(BaseAdmin):
    pass

@admin.register(IrrigationZone)
class IrrigationZoneAdmin(BaseAdmin):
    pass
