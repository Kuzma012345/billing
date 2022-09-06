from django.db import models


class Transaction(models.Model):
    STATUS = (
        ("Completed", "Completed"),
        ("Rejected", "Rejected")
    )

    order = models.CharField(max_length=512)
    amount = models.FloatField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    status = models.CharField(max_length=128, choices=STATUS)
    data = models.CharField(max_length=512)
