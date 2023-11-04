from django.db import models

# Create your models here.
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    Customer_Name= models.CharField(max_length=100,blank=False)
    Car_choices = (('Slavia', 'Slavia'), ('Khushaq', 'Khushaq'), ('Kodiaq', 'Kodiaq'), ('Superb', 'Superb'), ('Kamiq', 'Kamiq'))
    Car_Model= models.CharField(choices=Car_choices,max_length=50)
    Email= models.EmailField()
    Phone_Number= models.BigIntegerField()
    Registration_Number= models.CharField(max_length=100,blank=False)
    Options=(('Pickup Only','Pickup Only'),('Drop off Only','Drop off Only'),('Pickup and Drop Only','Pickup and Drop Only'),('Not Required','Not Required'))
    Pickup_and_Dropoff= models.CharField(choices=Options,max_length=50)
    Appointment_Date= models.DateField()

    def __str__(self):
        return self.Customer_Name

class CarOrders(models.Model):
    id = models.AutoField(primary_key=True)
    Customer_Name=models.CharField(max_length=100,blank=False)
    Car_choices = (('Slavia', 'Slavia'), ('Khushaq', 'Khushaq'), ('Kodiaq', 'Kodiaq'), ('Superb', 'Superb'), ('Kamiq', 'Kamiq'))
    Car_Model=models.CharField(choices=Car_choices,max_length=50)
    Email= models.EmailField()
    Phone_Number=models.BigIntegerField()

    def __str__(self):
        return self.Customer_Name
