from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now



class User(AbstractUser):
    email=models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.username}, {self.email}"

class Listing(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    start_bid=models.FloatField()
    pic=models.TextField(null=True)
    category=models.CharField(max_length=150, default="no category")
    created_date=models.DateTimeField(default=now, editable=False)
    #listing_owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Listing id:{self.id},{self.title}"


class Bid(models.Model):
    val=models.FloatField()

    def __str__(self):
        return f"{self.val} "