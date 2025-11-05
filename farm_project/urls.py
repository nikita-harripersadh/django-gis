from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Simple test view
def test_view(request):
    return HttpResponse("Hello, this is a test page!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('test/', test_view),         # Test page
]
