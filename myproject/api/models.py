from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    insurance_provider = models.CharField(max_length=100)
    insurance_number = models.CharField(max_length=100)
    diagnosis = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name
