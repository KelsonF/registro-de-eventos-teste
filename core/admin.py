from django.contrib import admin
from .models import Event, Attendance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ['name', 'date', 'location', 'access_code', 'created_by']
  list_filter = ['date', 'created_by']
  search_fields = ['name', 'location', 'access_code']
  readonly_fields = ['access_code']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
  list_display = ['guest_name', 'event', 'status', 'total_guests', 'confirmation_date']
  list_filter = ['status', 'event']
  search_fields = ['guest_name', 'event__name']