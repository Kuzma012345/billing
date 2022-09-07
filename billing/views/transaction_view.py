from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from billing.serializers.transaction_serializer import GetTransactionSerializer, ReturnTransactionSerializer
from billing.models.customer import Customer, Balance

from billing.models import Transaction


class TransactionView(APIView):
    
    def get(self, request):

        serializer = GetTransactionSerializer(data=request.GET)
        if serializer.is_valid():
            try:
                customer = Customer.objects.get(pk=serializer.validated_data['customer_id'])
                if serializer.validated_data['secret'] == customer.secret:
                    if Transaction.objects.filter(order=serializer.validated_data['order']).exists():
                        trans = Transaction.objects.get(order=serializer.validated_data['order'])
                        ser = \
                            ReturnTransactionSerializer(trans)
                        return Response(
                            {
                                "status": "success",
                                "Transaction": ser.data
                            }, status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {
                                "status": "error",
                                "message": f"Transaction with id {serializer.validated_data['order']}, does not exist"
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