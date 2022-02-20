from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now

from django.utils import timezone

class User(AbstractUser):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email=models.EmailField(max_length=254)
    date_joined = models.DateTimeField(default=timezone.now)





    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"



class RouteManager(models.Manager):
    def create_route(self, origin,destination,no_pass,date_orig,time_orig,time_dep,cost,thedriver,thepassenger):
        route=self.create(origin=origin,destination=destination,date_orig=date_orig,time_orig=time_orig,time_dep=time_dep,no_pass=no_pass,cost=cost,thedriver=thedriver,thepassenger=thepassenger)
        return route






class Route(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    date_orig=models.DateTimeField
    time_orig=models.TimeField
    time_dep=models.TimeField
    no_pass = models.IntegerField()
    cost=models.FloatField()
    thedriver=models.ForeignKey(User, on_delete=models.CASCADE, null="FALSE", blank="FALSE")
    thepassenger=models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE", related_name="passengers")

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} with {self.no_passengers} at {self.cost} per passenger"