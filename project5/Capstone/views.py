from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Count
from django.core.exceptions import ObjectDoesNotExist
from .forms import RouteForm
from .models import User
def index(request):
    return render(request, 'Capstone/index.html')


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
            return render(request, "Capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Capstone/login.html")


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
            return render(request, "Capstone/register.html", {
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
        return render(request, "Capstone/register.html")
@login_required
def passenger(request):
    return render(request, "Capstone/passenger.html")

@login_required
def driver(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RouteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            origin=request.POST["origin"]
            destination = request.POST["destination"]
            date_orig = request.POST["date_orig"]
            time_orig = request.POST["time_orig"]
            time_dep = request.POST["time_dep"]
            num_pass = request.POST["num_pass"]
            cost= request.POST["cost"]
            create_route(origin,destination,date_orig,time_orig,time_dep,num_pass,cost)
            # redirect to a new URL:
            return HttpResponseRedirect('driver')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RouteForm()

    return render(request, 'Capstone/driver.html', {'form': form})

def bing(request):
    return render(request, "Capstone/bing.html")


@login_required
def create_route(request,origin,destination,date_orig,time_orig,time_dep,num_pass,cost):

    created_date = timezone.now()



    description = request.POST["description"]

    driver = request.user



    myroute = Route.objects.create_post(description=description,created_date=created_date, owner=owner)



        return HttpResponseRedirect(reverse("index"))

    else:
        return render(reques