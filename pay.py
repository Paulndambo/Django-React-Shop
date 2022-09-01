import time
import datetime
import stripe

stripe.api_key = "sk_test_51JxuYcHqOVwxetFN4fSr6ijOL345B9iJLKgpfhTPVeI83YyhiE1EbALPWAX8gCKMpGCgoQkdeQWzlDuOZ3uBYenY00a7xbWY61"

ms = datetime.datetime.now().date()
#today_timestamp = time.mktime(ms.timetuple())
today_timestamp = time.mktime(ms.timetuple())
today_date = datetime.datetime.fromtimestamp(today_timestamp)


payments = stripe.PaymentIntent.search(
    query="status:'succeeded'",
    limit=5
)

print(payments)

