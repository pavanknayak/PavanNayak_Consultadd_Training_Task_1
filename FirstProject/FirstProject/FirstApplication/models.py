from django.db import models

# Create your models here.

class Name(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)

class ID(models.Model):
    number = models.CharField(max_length=10)

class Contact(models.Model):
    Phone_number = models.CharField(max_length=15)

class Address(models.Model):
    Street_address = models.CharField(max_length=70)



