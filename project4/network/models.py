from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now



class User(AbstractUser):
    email=models.EmailField(max_length=254)
    #picture_url=models.TextField(null=True)
    #followers=


    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"

class MypostManager(models.Manager):
    def create_post(self, description,created_date,owner):
        mypost=self.create(description=description,created_date=created_date, owner=owner)
        return mypost


class Mypost(models.Model):

    description=models.CharField(max_length=300)
    created_date=models.DateTimeField(default=now, editable=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    #users = models.ManyToManyField(User, blank="TRUE", related_name="listings")
    objects = MypostManager()
    def __str__(self):
        return f"Post id:{self.id},{self.title}"

# class BidManager(models.Manager):
#
#     def place_bid(self,val,bidder,listing_bid):
#         bid=self.create(val=val,bidder=bidder,listing_bid=listing_bid)
#         return bid




# class Bid(models.Model):
#     val=models.FloatField()
#     bidder=models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
#     listing_bid=models.ForeignKey(Listing, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
#     objects=BidManager()
#
#     def __str__(self):
#         return f"{self.val},{self.bidder}"



class CommentManager(models.Manager):

    def create_comment(self,comment_txt,post_comment,created_date,comment_author):
        comment=self.create(comment_txt=comment_txt, listing_comment=post_comment,created_date=created_date, comment_author=comment_author)
        return comment

class Comment(models.Model):
    comment_txt=models.CharField(max_length=150, blank="True")
    mypost_comment=models.ForeignKey(Mypost, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    created_date=models.DateTimeField(default=now, editable=False)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    objects = CommentManager()
    def __str__(self):
        return f"{self.comment_txt}"