from django import forms
from .models import FarmLocation, Crop, IrrigationZone

class FarmLocationForm(forms.ModelForm):
    class Meta:
        model = FarmLocation
        exclude = ['last_update', 'last_update_by']

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        exclude = ['last_update', 'last_update_by']

class IrrigationZoneForm(forms.ModelForm):
    class Meta:
        model = IrrigationZone
        exclude = ['last_update', 'last_update_by']
