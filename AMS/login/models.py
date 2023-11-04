from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return self.username

class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username

class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    Name_choices=(('Slavia','Slavia'),('Khushaq','Khushaq'),('Kodiaq','Kodiaq'),('Superb','Superb'),('Kamiq','Kamiq'))
    Name = models.CharField(max_length=50,choices=Name_choices)
    Model = models.CharField(max_length=100)
    Fuel_choices=(('Petrol','Petrol'),)
    Fuel = models.CharField(max_length=20,choices=Fuel_choices)
    Transmission_choices=(('Manual','Manual'),('Automatic','Automatic'))
    Transmission=models.CharField(max_length=50,choices=Transmission_choices)
    Mileage=models.FloatField()
    Engine_Displacement=models.IntegerField()
    Max_Power=models.FloatField()
    Seating_Capacity=models.IntegerField()
    Boot_Space=models.IntegerField()
    No_of_cylinder=models.IntegerField()
    Ground_Clearance=models.IntegerField()
    Max_Torque=models.IntegerField()
    Body_Type= models.CharField(max_length=50)
    Price=models.FloatField()

    def __str__(self):
        return self.Model