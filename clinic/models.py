from django.db import models


class MedicalHistory(models.Model):
    illness = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.illness


class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=200)
    contact = models.IntegerField( unique=True)
    medical_histories = models.ManyToManyField(MedicalHistory)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
