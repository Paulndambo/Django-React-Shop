from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import PaymentSerializer
from .models import Payment
import stripe
stripe.api_key = "sk_test_51JxuYcHqOVwxetFN4fSr6ijOL345B9iJLKgpfhTPVeI83YyhiE1EbALPWAX8gCKMpGCgoQkdeQWzlDuOZ3uBYenY00a7xbWY61"
from .pay import get_stripe_payments, get_payments

# Create your views here.
class PaymentAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def get(self, request):
        stripe_payments = get_stripe_payments()
        project_payments = get_payments()
        payments = Payment.objects.all()
        serializer = self.get_serializer(payments, many=True)
        print(stripe_payments)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        email = request.data.get('email')
        
        data = {
            "payment_ref": "234596",
            "name": "Ndambo Paul",
            "email": email,
            "currency": "USD",
            "amount": 1.00,
            "status": "failed",
            "date_paid": "2022-08-13"
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)