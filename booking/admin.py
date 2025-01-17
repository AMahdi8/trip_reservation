from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['destination', 'number_of_travelers']
    ordering = ['destination']
