from rest_framework import serializers


class ProductSerializer(serializers):
    name = serializers.CharField(max_length=512)
    customer = serializers.IntegerField()
    secret = serializers.CharField(max_length=100)

