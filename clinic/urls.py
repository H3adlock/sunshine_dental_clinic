from django.urls import path
from .views import MedicalHistoryListView, PatientSerializerListView, AppointmentSerializerListView, \
    PatientAppointmentSerializerListView

urlpatterns = [
    path('medical-history/', MedicalHistoryListView.as_view(), name='medical_history_list'),
    path('patients', PatientSerializerListView.as_view(), name='patients_list'),
    path('appointments', AppointmentSerializerListView.as_view(), name='appointments_list'),
    path('appointments/patients/', PatientAppointmentSerializerListView.as_view(), name='patients_appointment_list'),
]
