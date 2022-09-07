from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from billing.models.customer import Customer, Balance
from billing.models.products import Product

from billing.serializers.customer_serializer import CreateCustomerSerializer, GetCustomerSerializer
from billing.serializers.balance_serializer import GetBalanceSerializer

from billing.serializers.product_serializer import GetProductSerializer


class CustomerView(APIView):

    def post(self, request):

        serializer = CreateCustomerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                customer = Customer.objects.create(
                    name=serializer.validated_data['name'],
                    company=serializer.validated_data['company'],
                    secret=serializer.validated_data['secret']
                )
                balance_rub = Balance.objects.create(
                    customer=customer,
                    amount=0.0,
                    currency='RUB'
                )
                balance_usd = Balance.objects.create(
                    customer=customer,
                    amount=0.0,
                    currency='USD'
                )
                return Response(
                    {
                        "status": "success",
                        "customer": {
                            "customer_id": customer.pk,
                            "customer_name": customer.name,
                        }
                    }, status=status.HTTP_200_OK
                )
            except Exception as e:
                if "already exists" in str(e):
                    return Response(
                        {
                            "status": "error",
                            "message": f"Customer with name {serializer.validated_data['name']}, already exists"
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(
                {
                    "status": "error",
                    'field_errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        serializer = GetCustomerSerializer(data=request.GET)
        if serializer.is_valid():
            try:
                customer = Customer.objects.get(pk=serializer.validated_data['customer_id'])
                if customer.secret == serializer.validated_data['secret']:
                    balance = GetBalanceSerializer(Balance.objects.filter(customer_id=customer), many=True)
                    product = GetProductSerializer(Product.objects.filter(customer_id=customer), many=True)
                    return Response(
                        {
                            "status": "success",
                            "customer": {
                                "id": customer.pk,
                                "name": customer.name,
                                "company": customer.company,
                                "balance": balance.data,
                                "products": product.data
                            }
                        }, status=status.HTTP_200_OK
                    )
            except Exception as e:
                if "does not exist" in str(e):
                    return Response(
                        {
                            "status": "error",
                            "message": f"Customer with id {serializer.validated_data['customer_id']}, does not exist"
                        }, status=status.HTTP_400_BAD_REQUEST
                    )

                else:
                    return Response(
                        {
                            "status": "error",
                            "message": "Wrong signature"
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(
                {
                    "status": "error",
                    'field_errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )
