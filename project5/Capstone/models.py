from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now

from django.utils import timezone

class User(AbstractUser):
    email=models.EmailField(max_length=254)
    date_joined = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return f"{self.username}"
        #return f"{self.username}, {self.email}"
