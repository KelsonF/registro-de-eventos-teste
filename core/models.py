from django.db import models
from django.contrib.auth.models import User
from core.utils import generate_unique_access_code

# Create your models here.

class Event(models.Model):
  name = models.CharField(max_length=120)
  date = models.DateTimeField()
  location = models.CharField(max_length=250)
  description = models.TextField(blank=True)
  access_code = models.CharField(max_length=20, unique=True, editable=False)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    if not self.access_code:
      self.access_code = generate_unique_access_code()
    super().save(*args, **kwargs)

class Attendance(models.Model):
  STATUS_CHOICES = [
    ('confirmed', 'Confirmed'),
    ('declined', 'Declined'),
  ]

  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  guest_name = models.CharField(max_length=200)
  total_guests = models.PositiveIntegerField()
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)
  notes = models.TextField(blank=True)
  confirmation_date = models.DateTimeField(auto_now_add=True)