from django.urls import path, include
from views import plaintrip

urlpatterns = [
    path('plaintrip', plaintrip, name = 'plaintrip')
]