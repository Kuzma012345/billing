from rest_framework import serializers


class PaymentSerializer(serializers):
    order = serializers.CharField(max_length=512)
    amount = serializers.FloatField()
    customer_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    secret = serializers.CharField(max_length=100)
