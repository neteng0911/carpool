from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import User, Listing, Bid, Comment


def index(request):
    # return render(request, "auctions/index.html")
    return render(request, "auctions/index.html", {"listings": Listing.objects.all()})


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


def flisting(request, listing_id):

    listing = Listing.objects.get(id=listing_id)
    created_date = timezone.now()
    current_user=request.user
    comms = listing.comms.all()
    bids=Bid.objects.filter(listing_bid=listing_id)
    print(bids)
    max_bid = bids.aggregate(Max("val"))
    the_max_bid=max_bid["val__max"]
    print(max_bid)
    print(the_max_bid)
    highest_bid=bids.get(val=the_max_bid)
    highest_bidder=highest_bid.bidder
    print(highest_bidder)
    if request.method=="POST" and "place_bid" in request.POST:
        bid_val = request.POST["bid_val"]
        bidder = current_user
        listing_bid = listing
        bid = Bid.objects.place_bid(bid_val, bidder, listing_bid)
        bid.save()
        listing.price = bid_val
        listing.save()

        return render(request, "auctions/listings/flisting.html",
                      {"listing": listing, "message": "bid placed succesfully","comms":comms,"highest_bidder": highest_bidder})
    if request.method=="POST" and "submit_comment" in request.POST:
        comment_txt=request.POST["comment_input"]
        comment_author=current_user
        listing_comment=listing
        comment = Comment.objects.create_comment(
            comment_txt=comment_txt,
            comment_author=comment_author,
            created_date=created_date,
            listing_comment=listing_comment,
        )
        comment.save()
        comment.lists.add(listing)
        return render(request, "auctions/listings/flisting.html", {"listing": listing, "comms":comms,"highest_bidder": highest_bidder,
                                                                   "the_max_bid":the_max_bid})
    if request.method == "POST" and "close_auction" in request.POST:

        listing.closed_auction=True
        listing.winner=bid.bidder
        listing.message="This auction is closed"
        listing.save()



        return render(request, "auctions/listings/flisting.html", {"listing": listing, "comms": comms,
                                                                   "highest_bidder": highest_bidder,
                                                                   "the_max_bid":the_max_bid})
    else:

        return render(request, "auctions/listings/flisting.html", {"listing": listing,"comms":comms,"highest_bidder": highest_bidder,
                                                                   "the_max_bid":the_max_bid})


@login_required
def create_listing(request):
    # check if method is POST
    created_date = timezone.now()

    if request.method=="POST":
        title = request.POST["title"]
        description = request.POST["description"]
        picture_url = request.POST["picture_url"]
        price = request.POST["price"]
        category = request.POST["category"]
        listing_owner = request.user
        listing = Listing.objects.create_listing(title, description, price, picture_url, category, created_date,
                                                 listing_owner)
        listing.save()

        return render(request, "auctions/listings/flisting.html", {"listing": listing})

    else:
        return render(request, "auctions/create_listing.html", {"created_date": created_date})


@login_required
def my_listings(request):
    my_listings = Listing.objects.filter(listing_owner=request.user)
    # my_listings=listings.users.all()
    # my_listings=Listing.objects.get(listing_owner=request.user)
    return render(request, "auctions/my_listings.html", {"my_listings": my_listings})


@login_required
def watchlist(request):
    pass
