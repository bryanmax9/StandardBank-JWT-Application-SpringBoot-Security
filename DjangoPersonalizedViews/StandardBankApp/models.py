from django.db import models

# Define the database tables
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    membership = models.CharField(max_length=50)
    date_joined = models.DateTimeField()

class AppUsage(models.Model):
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usage_type = models.CharField(max_length=50)
    session_start = models.DateTimeField()
    session_end = models.DateTimeField()
    clicks = models.IntegerField()
    pages_visited = models.IntegerField()
    device = models.CharField(max_length=50)

class Transactions(models.Model):
    timestamp = models.DateTimeField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_transactions")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_transactions")
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
