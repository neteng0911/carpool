from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new",views.new, name="new"),
    path("random",views.random, name="random"),
    path("search_results",views.search_results, name="search_results"),

    path('<str:title>',views.entry, name='entry'),


]
