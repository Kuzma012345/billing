from rest_framework import serializers


class TransactionSerializer(serializers):
    order = serializers.CharField(max_length=512)
    customer_id = serializers.IntegerField()
    secret = serializers.CharField(max_length=512)
