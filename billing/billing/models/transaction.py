from django.db import models


class Transaction(models.Model):
    STATUS = (
        ("New", "New"),
        ("Completed", "Completed"),
        ("Rejected", "Rejected")
    )
    CURRENCY_CODE = (
        ("RUB", "RUB"),
        ("USD", "USD")
    )

    order = models.CharField(max_length=512, unique=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    status = models.CharField(max_length=128, choices=STATUS)
    currency = models.CharField(max_length=32, choices=CURRENCY_CODE)
    data = models.CharField(max_length=512)
