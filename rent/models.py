from django.db import models
from user.models import User
from car.models import Car
# Create your models here.


class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.IntegerField(null=True)


    def __str__(self):
        return (self.user.name+' - '+self.car.model)
