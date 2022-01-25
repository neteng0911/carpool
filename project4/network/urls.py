
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_post",views.create_post, name="create_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("edit/post/<int:post_id>", views.edit_post, name="edit_post"),
    path("like/post/<int:post_id>", views.like_post, name="like_post"),
    path("unlike/post/<int:post_id>", views.unlike_post, name="unlike_post"),
    path("following",views.following, name="following")

]
