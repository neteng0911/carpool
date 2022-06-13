from django.db import models

from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

from django.utils.timezone import now

from django.utils import timezone
import random
from datetime import date, datetime
import pytz




def random_string():
    return str(random.randint(10000, 99999))


class User(AbstractUser):

    email=models.EmailField(max_length=254)
    date_joined = models.DateTimeField(default=now)
    name = models.CharField(max_length=64, null=False, blank=False)
    surname = models.CharField(max_length=64, null=False, blank=False)
    profile_pic = models.ImageField(null=False, blank=False, default='/default_user.jpg')
    about = models.CharField(max_length=64, null=True, blank=True)
    dob = models.DateField(blank=False,default=date.today())


    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"






class RouteManager(models.Manager):
    def create_route(self, departure,destination,date_orig,time_orig,date_ret,time_dep,cost,no_pass,thedriver,map_pic,created_date,dist,d_a):
        route=self.create(departure=departure,destination=destination,date_orig=date_orig,time_orig=time_orig,date_ret=date_ret,
                          time_dep=time_dep,no_pass=no_pass,cost=cost,thedriver=thedriver,map_pic=map_pic,created_date=created_date,dist=dist, d_a=d_a)
        return route






class Route(models.Model):
    departure = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    date_orig=models.DateField("date orig")
    time_orig=models.TimeField("time orig")
    date_ret = models.DateField("date ret")
    time_dep=models.TimeField("time dep")
    no_pass = models.IntegerField()
    cost=models.FloatField()
    thedriver=models.ForeignKey(User, on_delete=models.CASCADE, null="FALSE", blank="FALSE")
    map_pic = models.CharField(max_length=256,null=True)
    created_date = models.DateTimeField(default=now, editable=False)
    thepassenger = models.ManyToManyField(User, blank="TRUE", related_name="thepassengers")
    fin_set = models.BooleanField(default=False) # if the driver wants to manually close the trip
    keynum = models.CharField(max_length=12, default = random_string)
    dist = models.FloatField(blank = 'TRUE')
    d_a = models.BooleanField(default=False) # whether the vehicle has disability access

    




#  workaround method so as to auto-close the trips depending on the current date and time (if the have expired or started or no available seats exist)
    def fin(self):


        if self.date_orig < datetime.now().date() :
            return True
        elif self.date_orig == datetime.now().date() and self.time_orig < datetime.now().time():
            return True

        else:
            return False


    def fin_p(self):
        if self.no_pass == self.thepassenger.count():
            return True




    objects = RouteManager()
    marker=object()
    def __str__(self):
        return f"{self.id}: {self.departure} to {self.destination} with {self.no_pass} at {self.cost} per passenger"



# method for auto calculating the cost per passenger in the DB
    def costpp(self, est_cost=marker):
        while self.thepassenger.all().count()<=self.no_pass:
            if self.thepassenger.all().count()==0:
                est_cost=self.cost
            else:
                est_cost=self.cost/self.thepassenger.all().count()
            return est_cost
        else:
            est_cost=self.cost/self.no_pass
        return est_cost


# so as to interact with javascript with fetch method
    def serialize(self):
        return{

            'departure':self.departure,
            'destination':self.destination,
            'date_orig':self.date_orig,
            'time_orig':self.time_orig,
            'time_dep':self.time_dep,
            'no_pass':self.no_pass,
            'cost':self.cost,

            'map_pic':self.map_pic,
            'created_date':self.created_date,
            'dist': self.dist,
            'key_num':self.keynum



        }



class CommentManager(models.Manager):

    def create_comment(self,comm_txt,route_comm,created_date,owner):
        comment=self.create(comm_txt=comm_txt, route_comm=route_comm,created_date=created_date, owner=owner)
        return comment

class Comment(models.Model):
    comm_txt=models.CharField(max_length=150, blank="True")
    route_comm=models.ForeignKey(Route, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    created_date=models.DateTimeField(default=now, editable=False)
    lists = models.ManyToManyField(Route, blank="TRUE", related_name="comments")  # make comment
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    objects = CommentManager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.comm_txt}"



class MessageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(created_date__gte=timezone.now()-timezone.timedelta(days = 7))#custom queryset to hide older than 7 days messages

class Message(models.Model):
    content = models.CharField(max_length=150, blank='True')
    recipient = models.ManyToManyField(User, related_name='messages')
    created_date=models.DateTimeField(default=now, editable=False)
    route_id= models.IntegerField()

    objects = MessageManager()







class Qrcode(models.Model):
    code = models.CharField(max_length=12, default = random_string)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE", related_name='code')
    trip = models.ManyToManyField(Route, related_name='qrcodes')
