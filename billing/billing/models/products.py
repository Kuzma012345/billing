from django.db import models
from .customer import Customer


class Product(models.Model):
    name = models.CharField(max_length=512)
    value = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
