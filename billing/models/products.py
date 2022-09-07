from django.db import models
from .customer import Customer


class Product(models.Model):
    CURRENCY_CODE = (
        ("RUB", "RUB"),
        ("USD", "USD")
    )

    name = models.CharField(max_length=512, unique=True)
    value = models.FloatField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.CharField(max_length=32, choices=CURRENCY_CODE, default="RUB")