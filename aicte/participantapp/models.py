from django.db import models

# Create your models here.
class ParticipantGeneralDetails(models.Model):
    username = models.CharField(max_length=200)
    eventid =models.CharField(max_length=200)
    eventname =models.CharField(max_length=200)
    phoneno =models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dob = models.DateField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    state = models.CharField(max_length=500)
    alternameemail = models.CharField(max_length=200)
    whatsappnumber = models.CharField(max_length=50)