from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField(default=10)

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=255) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name