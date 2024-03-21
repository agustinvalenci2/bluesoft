# In admin.py of each app

from django.contrib import admin
from .models import Client  # Import your models here

admin.site.register(Client)  # Register your models here
