
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("passenger", views.passenger, name="passenger"),
    path("driver", views.driver, name="driver"),
    path("bing", views.bing, name="bing"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("edit/route/<int:route_id>", views.edit_route, name="edit_route"),
    path("join/route/<int:route_id>", views.join_route, name="join_route"),
    path("leave/route/<int:route_id>", views.leave_route, name="leave_route")

]
