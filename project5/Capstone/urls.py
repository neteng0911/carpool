
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("passenger", views.passenger, name="passenger"),
    path("driver", views.driver, name="driver"),
    path("bing", views.bing, name="bing")

]