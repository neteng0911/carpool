from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now



class User(AbstractUser):
    email=models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"

class ListingManager(models.Manager):
    def create_listing(self, title,description,start_bid,picture_url,category,created_date,listing_owner):
        listing=self.create(title=title, description=description,start_bid=start_bid,picture_url=picture_url,category=category,created_date=created_date, listing_owner=listing_owner)
        return listing


class Listing(models.Model):

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    start_bid=models.FloatField()
    picture_url=models.TextField(null=True)
    category=models.CharField(max_length=150, default="no category")
    created_date=models.DateTimeField(default=now, editable=False)
    listing_owner=models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ListingManager()
    def __str__(self):
        return f"Listing id:{self.id},{self.title}"

class BidManager(models.Manager):

    def place_bid(self,val,bidder,listing_bid):
        bid=self.create(val=val,bidder=bidder,listing_bid=listing_bid)
        return bid


class Bid(models.Model):
    val=models.FloatField()
    bidder=models.ForeignKey(User, on_delete=models.CASCADE)
    listing_bid=models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.val},{self.bidder} "