from rest_framework import serializers


class GetTransactionSerializer(serializers.Serializer):
    order = serializers.CharField(max_length=512)
    customer_id = serializers.IntegerField()
    secret = serializers.CharField(max_length=512)


class ReturnTransactionSerializer(serializers.Serializer):
    order = serializers.CharField(max_length=512)
    status = serializers.CharField(max_length=32)
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=32)
