from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import User, Listing, Bid
from datetime import date


def index(request):
    #return render(request, "auctions/index.html")
    return render(request, "auctions/index.html",{"listings":Listing.objects.all()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def flisting(request,listing_id):
    user = request.user
    listing=Listing.objects.get(id=listing_id)
    return render(request, "auctions/listings/flisting.html",{"listing":listing,"user":user})

def create_listing(request):
    # check if method is POST
    created_date = timezone.now()
    if request.method=="POST":

        title=request.POST["title"]
        description=request.POST["description"]
        picture_url=request.POST["picture_url"]
        start_bid = request.POST["start_bid"]
        category = request.POST["category"]
        listing_owner=request.user
        listing = Listing.objects.create_listing(title,description,start_bid,picture_url,category,created_date,listing_owner)
        listing.save()
        return render(request, "auctions/listings/flisting.html",{"listing":listing})
    else:
        return render(request, "auctions/create_listing.html",{"created_date":created_date})
