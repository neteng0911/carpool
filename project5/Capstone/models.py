from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now

from django.utils import timezone

class User(AbstractUser):
    email=models.EmailField(max_length=254)
    date_joined = models.DateTimeField(default=timezone.now)
    following = models.ManyToManyField("User", blank="TRUE", related_name="followers")



    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"


class Route(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    no_passengers = models.IntegerField()
    date_orig=models.DateTimeField
    date_dep=models.DateTimeField

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"