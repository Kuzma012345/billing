from rest_framework import serializers


class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=512)
    customer_id = serializers.IntegerField()
    value = serializers.FloatField()
    secret = serializers.CharField(max_length=100)
    currency = serializers.CharField(max_length=32)

class GetProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=512)
    value = serializers.FloatField()
    currency = serializers.CharField(max_length=32)