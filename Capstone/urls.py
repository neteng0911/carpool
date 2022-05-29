
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
    path("leave/route/<int:route_id>", views.leave_route, name="leave_route"),
    path("route/<int:route_id>", views.load_route, name="load_route"),
    path("wroute/<int:route_id>", views.webload_route, name="webload_route"),
    path("valid-trips", views.find_valid_trips, name="valid_trips"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),



]
