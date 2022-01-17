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
        return f"Post id:{self.id},{self.description}"


class ReplyManager(models.Manager):

    def create_reply(self,reply_txt,mypost_reply,created_date,owner,):
        reply=self.create(reply_txt=reply_txt, mypost_reply=mypost_reply,created_date=created_date, owner=owner)
        return reply

class Reply(models.Model):
    reply_txt=models.CharField(max_length=150, blank="True")
    mypost_reply=models.ForeignKey(Mypost, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    created_date=models.DateTimeField(default=now, editable=False)
    lists = models.ManyToManyField(Mypost, blank="TRUE", related_name="replies")  # post_reply
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null="TRUE", blank="TRUE")
    objects = ReplyManager()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.reply_txt}"