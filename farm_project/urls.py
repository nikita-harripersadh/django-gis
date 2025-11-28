from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect root URL '/' to '/farms/' (your main list view)
    path('', lambda request: redirect('farm:farm_list'), name='home'),

    # Farm app URLs
    path('', include('farm.urls')),  
]