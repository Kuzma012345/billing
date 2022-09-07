from rest_framework import serializers


class GetBalanceSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=32)

