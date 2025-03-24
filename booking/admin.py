from django.contrib import admin
from .models import Facility, Booking

# Register your models here.

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')
    list_filter = ('location',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'facility', 'date', 'status')
    list_filter = ('facility', 'date', 'status', 'user')
    search_fields = ('user__username', 'facility__name')  # Search by user's username and facility name
    date_hierarchy = 'date'
