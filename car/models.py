from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    licence_number = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    base_price = models.IntegerField()
    price_per_hour = models.IntegerField()
    deposit = models.IntegerField()

    def __str__(self):
        return self.licence_number
