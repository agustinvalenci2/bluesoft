# In admin.py of each app

from django.contrib import admin
from .models import Account, Transaction  # Import your models here

admin.site.register(Account)  # Register your models here
admin.site.register(Transaction )  # Register your models here