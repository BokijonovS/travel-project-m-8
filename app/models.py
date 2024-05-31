from django.db import models

# Create your models here.


class Travel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    tariff = models.CharField(max_length=100)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name



