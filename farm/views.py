from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import FarmLocation, Crop, IrrigationZone
from .forms import FarmLocationForm, CropForm, IrrigationZoneForm

# -------------------
# FarmLocation Views
# -------------------
def farm_list(request):
    locations = FarmLocation.objects.all()
    paginator = Paginator(locations, 10)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'farm/farmlocation_list.html', {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    })

def farm_detail(request, pk):
    location = get_object_or_404(FarmLocation, pk=pk)
    return render(request, 'farm/farmlocation_detail.html', {'object': location})

def farm_create(request):
    if request.method == 'POST':
        form = FarmLocationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_update_by = request.user
            obj.save()
            messages.success(request, "Farm location created successfully!")
            return redirect('farm:farm_list')
    else:
        form = FarmLocationForm()
    return render(request, 'farm/farmlocation_form.html', {'form': form})

def farm_update(request, pk):
    location = get_object_or_404(FarmLocation, pk=pk)
    if request.method == 'POST':
        form = FarmLocationForm(request.POST, instance=location)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_update_by = request.user
            obj.save()
            messages.success(request, "Farm location updated successfully!")
            return redirect('farm:farm_list')
    else:
        form = FarmLocationForm(instance=location)
    return render(request, 'farm/farmlocation_form.html', {'form': form})

def farm_delete(request, pk):
    location = get_object_or_404(FarmLocation, pk=pk)
    if request.method == 'POST':
        location.delete()
        messages.success(request, "Farm location deleted successfully!")
        return redirect('farm:farm_list')
    return render(request, 'farm/farmlocation_confirm_delete.html', {'object': location})


# -------------------
# Crop Views
# -------------------
def crop_list(request):
    crops = Crop.objects.all()
    paginator = Paginator(crops, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'farm/crop_list.html', {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    })

def crop_detail(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    return render(request, 'farm/crop_detail.html', {'object': crop})

def crop_create(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_update_by = request.user
            obj.save()
            messages.success(request, "Crop created successfully!")
            return redirect('farm:crop_list')
    else:
        form = CropForm()
    return render(request, 'farm/crop_form.html', {'form': form})

def crop_update(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_update_by = request.user
            obj.save()
            messages.success(request, "Crop updated successfully!")
            return redirect('farm:crop_list')
    else:
        form = CropForm(instance=crop)
    return render(request, 'farm/crop_form.html', {'form': form})

def crop_delete(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        crop.delete()
        messages.success(request, "Crop deleted successfully!")
        return redirect('farm:crop_list')
    return render(request, 'farm/crop_confirm_delete.html', {'object': crop})


# -------------------
# IrrigationZone Views
# -------------------
def zone_list(request):
    zones = IrrigationZone.objects.all()
    paginator = Paginator(zones, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'farm/zone_list.html', {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    })

def zone_detail(request, pk):
    zone = get_object_or_404(IrrigationZone, pk=pk)
    return render(request, 'farm/zone_detail.html', {'object': zone})

def zone_create(request):
    if request.method == 'POST':
        form = IrrigationZoneForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_update_by = request.user
            obj.save()
            messages.success(request, "Irrigation zone created successfully!")
            return redirect('farm:zone_list')
    else:
        form = IrrigationZoneForm()
    return render(request, 'farm/zone_form.html', {'form': form})

def zone_update(request, pk):
    zone = get_object_or_404(IrrigationZone, pk=pk)
    if request.method == 'POST':
        form = IrrigationZoneForm(request.POST, instance=zone)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_update_by = request.user
            obj.save()
            messages.success(request, "Irrigation zone updated successfully!")
            return redirect('farm:zone_list')
    else:
        form = IrrigationZoneForm(instance=zone)
    return render(request, 'farm/zone_form.html', {'form': form})

def zone_delete(request, pk):
    zone = get_object_or_404(IrrigationZone, pk=pk)
    if request.method == 'POST':
        zone.delete()
        messages.success(request, "Irrigation zone deleted successfully!")
        return redirect('farm:zone_list')
    return render(request, 'farm/zone_confirm_delete.html', {'object': zone})
