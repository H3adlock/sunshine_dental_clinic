from rest_framework import serializers
from .models import MedicalHistory, Patient, Appointment


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        depth = 1


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class PatientAppointmentSerializer(serializers.ModelSerializer):
    appointment_patient = AppointmentSerializer(source='appointment_set', many=True)

    class Meta:
        model = Patient
        fields = ('id', 'name', 'age', 'address', 'occupation', 'contact', 'medical_histories', 'appointment_patient')
        depth = 1
