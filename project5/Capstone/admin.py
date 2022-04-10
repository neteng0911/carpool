from django.contrib import admin
from .models import Route, Comment, User, Message

# Register your models here.

admin.site.register(Route)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Message)
