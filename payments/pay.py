import stripe
stripe.api_key = "sk_test_51JxuYcHqOVwxetFN4fSr6ijOL345B9iJLKgpfhTPVeI83YyhiE1EbALPWAX8gCKMpGCgoQkdeQWzlDuOZ3uBYenY00a7xbWY61"
from datetime import datetime
from .models import Payment


def get_payments():
    payments = Payment.objects.all().values_list('payment_ref', flat=True)
    return payments

def get_stripe_payments():
    payments_collected = []
    try:
        payments = stripe.PaymentIntent.search(
            query="status:'succeeded'",
            limit = 5
        )
        if payments:
            for payment in payments:
                charges = payment['charges']['data']
                for x in charges:
                    billing = x['billing_details']
                    payment_object = {
                        "payment_ref": payment['id'],
                        "amount": payment['amount'],
                        "status": payment['status'],
                        "email": billing['email'],
                        "name": billing['name'],
                        "currency": payment['currency'],
                        "date_paid": datetime.fromtimestamp(payment["created"]).date(),
                    }
                    payments_collected.append(payment_object)
        else:
            print("No Payments")
        
    except Exception as e:
        raise e

    existing_payment_refs = get_payments()
    new_payments = [payment for payment in payments_collected if payment['payment_ref'] not in existing_payment_refs]
    try:
        for payment in new_payments:
            payment = Payment.objects.create(**payment)
    except Exception as e:
        raise e
    return new_payments


