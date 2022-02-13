from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now

from django.utils import timezone

class User(AbstractUser):
    email=models.EmailField(max_length=254)
    date_joined = models.DateTimeField(default=timezone.now)
    routes = models.ManyToManyField(Route, blank=True, related_name="passengers")




    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"



class RouteManager(models.Manager):
    def create_route(self, origin,destination,no_passengers,date_orig,date_dep,driver):
        route=self.create(origin=origin,created_date=created_date, owner=owner)
        return route






class Route(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    no_passengers = models.IntegerField()
    date_orig=models.DateTimeField
    date_dep=models.DateTimeField
    cost=models.FloatField()
    driver=models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    passenger=models.ForeignKey(User, null="TRUE", blank="TRUE")

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} with {self.no_passengers} at {self.cost} per passenger"