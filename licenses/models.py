# licenses/models.py
from django.db import models

class License(models.Model):
    key = models.CharField(max_length=80, unique=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.key
