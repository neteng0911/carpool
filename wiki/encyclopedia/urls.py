from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new",views.new, name="new"),
    path("random_entry",views.random_entry, name="random_entry"),
    path("search_results",views.search_results, name="search_results"),
    path("edit_entry/<str:title>",views.edit_entry, name="edit_entry"),

    path('<str:title>',views.entry, name='entry'),


]
