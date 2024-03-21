from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.urls import path
from .views import ClientListView,ClientDetailView
urlpatterns = [
    path('view',ClientListView.as_view()),
    path('details/<int:client_id>',ClientDetailView.as_view()),
]
