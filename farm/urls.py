from django.urls import path
from . import views

app_name = 'farm'

urlpatterns = [
    # FarmLocation URLs
    path('farms/', views.farm_list, name='farm_list'),
    path('farms/add/', views.farm_create, name='farm_create'),
    path('farms/<int:pk>/', views.farm_detail, name='farm_detail'),
    path('farms/<int:pk>/edit/', views.farm_update, name='farm_update'),
    path('farms/<int:pk>/delete/', views.farm_delete, name='farm_delete'),

    # Crop URLs
    path('crops/', views.crop_list, name='crop_list'),
    path('crops/add/', views.crop_create, name='crop_create'),
    path('crops/<int:pk>/', views.crop_detail, name='crop_detail'),
    path('crops/<int:pk>/edit/', views.crop_update, name='crop_update'),
    path('crops/<int:pk>/delete/', views.crop_delete, name='crop_delete'),

    # IrrigationZone URLs
    path('zones/', views.zone_list, name='zone_list'),
    path('zones/add/', views.zone_create, name='zone_create'),
    path('zones/<int:pk>/', views.zone_detail, name='zone_detail'),
    path('zones/<int:pk>/edit/', views.zone_update, name='zone_update'),
    path('zones/<int:pk>/delete/', views.zone_delete, name='zone_delete'),
]
