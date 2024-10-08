# licenses/urls.py
from django.urls import path
from .views import ValidateLicense

urlpatterns = [
    path('validate/', ValidateLicense.as_view(), name='validate_license'),
]
