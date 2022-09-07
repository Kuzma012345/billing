from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from billing.models.customer import Customer
from billing.models.products import Product
from billing.serializers.product_serializer import CreateProductSerializer


class ProductView(APIView):

    def post(self, request):

        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                print(serializer.data)
                customer = Customer.objects.get(pk=serializer.validated_data['customer_id'])
                if customer.secret == serializer.validated_data['secret']:
                    if not Product.objects.filter(name=serializer.validated_data['name']).exists():
                        product = Product.objects.create(
                            name=serializer.validated_data['name'],
                            value=serializer.validated_data['value'],
                            customer_id=customer,
                            currency=serializer.validated_data['currency']
                        )
                        print(product.pk)
                        return Response(
                            {
                                "status": "success",
                                "id": product.pk
                            }, status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {
                                "status": "error",
                                "message": f"product with name {serializer.validated_data['name']} exists"
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