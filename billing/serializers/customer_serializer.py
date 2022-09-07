from rest_framework import serializers


class CreateCustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    secret = serializers.CharField(max_length=100)

class GetCustomerSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    secret = serializers.CharField(max_length=100)