from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Count
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Mypost, Reply



def index(request):
    all_posts=Mypost.objects.all()
    return render(request, "network/index.html", {"all_posts": all_posts}) # to set following posts not all posts later



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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



@login_required
def create_post(request):
    # check if method is POST
    created_date = timezone.now()

    if request.method=="POST":

        description = request.POST["description"]

        owner = request.user


        mypost = Mypost.objects.create_post(description=description,created_date=created_date, owner=owner)



        return render(request, "network/index.html", {"post": mypost})

    else:
        return render(request, "network/create_post.html", {"created_date": created_date})


@login_required
def reply(request, mypost_id):
    # check if method is POST
    created_date = timezone.now()

    if request.method == "POST":

        reply_txt = request.POST["reply_txt"]

        owner = request.user


        mypost_reply=Mypost.objects.get(id=mypost_id)     #AYTO DEN DOULEVEI ΨΑΧΝΩ ΤΟ ID ΤΟΥ ΠΟΣΤ ΠΟΥ ΘΑ ΚΑΝΩ REPLY

        reply = Reply.objects.create_reply(reply_txt=reply_txt, created_date=created_date, owner=owner, mypost_reply=my_post_reply)

        return render(request, "network/index.html", {"reply": reply})

    else:
        return render(request, "network/index.html", {"created_date": created_date})