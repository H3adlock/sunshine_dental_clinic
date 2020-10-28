from .models import MedicalHistory, Patient, Appointment
from .serializers import MedicalHistorySerializer, PatientSerializer, AppointmentSerializer, \
    PatientAppointmentSerializer
from rest_framework import generics
from .permissions import IsAdminOrReadOnly


class MedicalHistoryListView(generics.ListCreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class PatientSerializerListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AppointmentSerializerListView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PatientAppointmentSerializerListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientAppointmentSerializer
    permission_classes = (IsAdminOrReadOnly,)

class PatientAppointmentSerializerUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientAppointmentSerializer
    permission_classes = (IsAdminOrReadOnly,)