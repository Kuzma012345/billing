from rest_framework import serializers


class WithdrawalSerializer():
    customer_id = serializers.IntegerField()
    currency = serializers.CharField(max_length=32)
    secret = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
