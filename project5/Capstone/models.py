from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

from django.utils.timezone import now

from django.utils import timezone

class User(AbstractUser):

    email=models.EmailField(max_length=254)
    date_joined = models.DateTimeField(default=timezone.now)





    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"



class RouteManager(models.Manager):
    def create_route(self, origin,destination,date_orig,time_orig,time_dep,cost,no_pass,thedriver,map_pic,created_date):
        route=self.create(origin=origin,destination=destination,date_orig=date_orig,time_orig=time_orig,
                          time_dep=time_dep,cost=cost,no_pass=no_pass,thedriver=thedriver,map_pic=map_pic,created_date=created_date)
        return route






class Route(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    date_orig=models.DateTimeField("date orig", default=date.today())
    time_orig=models.TimeField("time orig",default=timezone.now())
    time_dep=models.TimeField("time dep",default=timezone.now())
    no_pass = models.IntegerField()
    cost=models.FloatField()
    thedriver=models.ForeignKey(User, on_delete=models.CASCADE, null="FALSE", blank="FALSE")
    map_pic = models.CharField(max_length=256,null=True)
    created_date = models.DateTimeField(default=now, editable=False)
    thepassenger = models.ManyToManyField(User, blank="TRUE", related_name="thepassengers")

    objects = RouteManager()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} with {self.no_passengers} at {self.cost} per passenger"



class ReplyManager(models.Manager):

    def create_reply(self,reply_txt,mypost_reply,created_date,owner,):
        reply=self.create(reply_txt=reply_txt, mypost_reply=mypost_reply,created_date=created_date, owner=owner)
        return reply

class Reply(models.Model):
    reply_txt=models.CharField(max_length=150, blank="True")
    myroute_reply=models.ForeignKey(Route, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    created_date=models.DateTimeField(default=now, editable=False)
    lists = models.ManyToManyField(Route, blank="TRUE", related_name="replies")  # post_reply
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    objects = ReplyManager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.reply_txt}"