from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    company = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"


class Balance(models.Model):
    CURRENCY_CODE = (
        ("RUB", "RUB"),
        ("USD", "USD")
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=32, choices=CURRENCY_CODE)
