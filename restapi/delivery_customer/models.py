from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Gabarits(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    cost = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    type = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    fio = models.CharField(max_length=256, null=False, blank=False)
    address_a = models.CharField(max_length=256, null=False, blank=False)
    address_b = models.CharField(max_length=256, null=False, blank=False)
    gabarits = models.ForeignKey(Gabarits, to_field='name',on_delete=models.CASCADE, null=False, blank=False)
    weigth = models.FloatField(null=True, blank=True)
    status = models.ForeignKey(Status, to_field='name', on_delete=models.SET_NULL, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)


