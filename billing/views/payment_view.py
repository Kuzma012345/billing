from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from billing.models import Customer
from billing.serializers.payment_serializer import PaymentSerializer

from billing.models import Product, Transaction

from billing.models import Balance


class PaymentView(APIView):

    def post(self, request):

        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                customer = Customer.objects.get(pk=serializer.validated_data['customer_id'])
                if customer.secret == serializer.validated_data['secret']:
                    if Product.objects.filter(customer_id=customer,
                                              pk=serializer.validated_data['product_id']).exists():
                        product = Product.objects.get(pk=serializer.validated_data['product_id'])
                        if product.currency == serializer.validated_data['currency']:
                            if not Transaction.objects.filter(order=serializer.validated_data['order']).exists():
                                transaction = Transaction.objects.create(
                                    order=serializer.validated_data['order'],
                                    amount=serializer.validated_data['amount'],
                                    currency=serializer.validated_data['currency'],
                                    status="New"
                                )
                                if serializer.validated_data['amount'] == product.value:
                                    transaction.status = "Completed"
                                    transaction.save()
                                    balance = Balance.objects.get(customer=customer,
                                                                  currency=serializer.validated_data['currency'])
                                    balance.amount = balance.amount + serializer.validated_data['amount']
                                    balance.save()
                                    return Response(
                                        {
                                            "status": "success",
                                            "transaction_id": transaction.pk
                                        }, status=status.HTTP_200_OK
                                    )
                                else:
                                    transaction.status = "Rejected"
                                    transaction.save()
                                    return Response(
                                        {
                                            "status": "failed",
                                            "transaction_id": transaction.pk,
                                            "message": "payment sum must be equal to product value"
                                        }, status=status.HTTP_400_BAD_REQUEST
                                    )
                            else:
                                return Response(
                                    {
                                        "status": "error",
                                        "message": f"Order with id {serializer.validated_data['order']} already exists"
                                    }, status=status.HTTP_400_BAD_REQUEST
                                )
                        else:
                            return Response(
                                {
                                    "status": "error",
                                    "message": f"Cannot provide payment with currency "
                                               f"{serializer.validated_data['currency']}"
                                }, status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {
                                "status": "error",
                                "message": "Product does not exist"
                            }, status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {
                            "status": "error",
                            "message": "Wrong signature"
                        }, status=status.HTTP_400_BAD_REQUEST
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
                    'field_errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )