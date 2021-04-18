from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now



class User(AbstractUser):
    email=models.EmailField(max_length=254)


    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"

class ListingManager(models.Manager):
    def create_listing(self, title,description,price,picture_url,category,created_date,listing_owner):
        listing=self.create(title=title, description=description,price=price,picture_url=picture_url,
                            category=category,created_date=created_date, listing_owner=listing_owner,closed_auction=closed_auction,
                            listing_message=listing_message)
        return listing


class Listing(models.Model):

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    price=models.FloatField()
    picture_url=models.TextField(null=True)
    category=models.CharField(max_length=150, default="no category")
    created_date=models.DateTimeField(default=now, editable=False)
    listing_owner=models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    closed_auction=models.CharField(max_length=5, default="False")
    listing_message=models.CharField(max_length=100, blank="TRUE")
    objects = ListingManager()
    def __str__(self):
        return f"Listing id:{self.id},{self.title}"

class BidManager(models.Manager):

    def place_bid(self,val,bidder,listing_bid):
        bid=self.create(val=val,bidder=bidder,listing_bid=listing_bid)
        return bid




class Bid(models.Model):
    val=models.FloatField()
    bidder=models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE",related_name="bidders")
    listing_bid=models.ForeignKey(Listing, on_delete=models.CASCADE, null="TRUE", blank="TRUE", related_name="listings_bidded")
    objects=BidManager()

    def __str__(self):
        return f"{self.val},{self.bidder}"



class CommentManager(models.Manager):

    def create_comment(self,comment_txt,listing_comment,created_date,comment_author):
        comment=self.create(comment_txt=comment_txt, listing_comment=listing_comment,created_date=created_date, comment_author=comment_author)
        return comment

class Comment(models.Model):
    comment_txt=models.CharField(max_length=150, blank="True")
    listing_comment=models.ForeignKey(Listing, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    created_date=models.DateTimeField(default=now, editable=False)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    lists = models.ManyToManyField(Listing, blank="TRUE", related_name="comms")
    #lists = models.ForeignKey(Listing, on_delete=models.CASCADE,null="TRUE", blank="TRUE", related_name="comms")
    objects = CommentManager()
    def __str__(self):
        return f"{self.comment_txt}"