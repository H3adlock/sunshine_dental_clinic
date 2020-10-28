from django.contrib import admin
from .models import Patient, MedicalHistory, Appointment

admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(Appointment)
