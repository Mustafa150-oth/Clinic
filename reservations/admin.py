from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Appointment, Complaint

admin.site.register(Appointment)
admin.site.register(Complaint)