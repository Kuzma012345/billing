from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    order = serializers.CharField(max_length=512)
    amount = serializers.FloatField()
    customer_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    currency = serializers.CharField(max_length=32)
    secret = serializers.CharField(max_length=100)
