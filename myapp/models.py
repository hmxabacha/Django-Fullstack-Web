from django.db import models

# Create your models here.

class BookingModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    reservation_date=models.DateField()
    reservation_time=models.TimeField()
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.reservation_date}{self.reservation_time}"
    
