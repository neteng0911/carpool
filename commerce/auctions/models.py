from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    date_joined=models.DateField()

    def __str__(self):
        return f"{self.first_name}, {self.last_name} joined on {self.date_joined}"

class Listing(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    start_bid=models.FloatField()

    def __str__(self):
        return f"Listing id:{self.id},{self.title}"


class Bid(models.Model):
    val=models.FloatField()

    def __str__(self):
        return f"{self.val}\u20ac35."