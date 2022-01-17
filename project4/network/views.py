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
    all_posts=Mypost.objects.order_by('-created_date')
    # check if method is POST
    created_date = timezone.now()


    owner = request.user

    replies = Reply.objects.order_by('-created_date')



    if request.method == "POST" and "post_reply" in request.POST:
        reply_txt = request.POST["reply_txt"]
        mypost_reply = request.POST.get("post_id")
        mypost = Mypost.objects.get(id=mypost_reply)

        my_post_replies = Reply.objects.filter(mypost_reply=mypost_reply)
        print(my_post_replies)
        reply = Reply.objects.create_reply(reply_txt=reply_txt, created_date=created_date, owner=owner,
                                           mypost_reply=mypost)
        reply.save()
        print(reply)
        reply.lists.add(mypost)
        print(owner, "replied on post number", mypost_reply, "and said:",reply)
        return render(request, "network/index.html", {"all_posts": all_posts, "replies":replies})




        #here first loads the post in different page before editing it BUT i display it as edit post on the page for the user
    if request.method == "POST" and "load_post" in request.POST:

        post_to_load_id = request.POST.get("post_to_load_id")
        post_to_load = Mypost.objects.get(pk=post_to_load_id)

        #load_post(post_to_load_id)

        return render(request, "network/post.html", {"post_to_load": post_to_load})

    else:
        return render(request, "network/index.html", {"all_posts": all_posts,"replies":replies})





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



        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "network/create_post.html", {"created_date": created_date})
#mporei na mhn xreiazetai check!!!!
def load_post(request, post_id):
    pass
    # post_to_load = Mypost.objects.get(pk=post_id)
    # print("loading post no",post_id)
    # return render(request, "network/post.html", {"post_to_load": post_to_load})

#mporei na mhn xreiazetai check!!!!


def edit_post(request, post_id):

    post_to_load = Mypost.objects.get(pk=post_id)
    if request.method =="POST" and "edit_post" in request.POST:

        edit_txt = request.POST["edit_txt"]
        post_to_load.description=edit_txt
        post_to_load.save()

        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST" and "del_post" in request.POST:
        post_to_load.delete()
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "network/post.html",{"post_to_load":post_to_load})


@login_required
def profile(request, user_id):
    current_user = request.user
    targ_user = User.objects.get(id=user_id)
    user_posts=Mypost.objects.filter(owner_id=user_id)
    user_posts_count=user_posts.count()


    myfollowinglist=current_user.following.all()
    followinglist =targ_user.following.all()
    followerslist = User.objects.filter(following=user_id)
    no_of_followers=len(followerslist)
    no_of_following=followinglist.count()
    print( targ_user,"Your followers are", followerslist)

    print("8888888888888")
    print(targ_user,"is following",followinglist)
    message=""
    if targ_user in myfollowinglist: #or listing in Listing.objects.filter(listing_owner=request.user):

        print(request.user,"you are following user", targ_user)


    created_date = timezone.now()




    if request.method=="POST" and "follow" in request.POST:
        current_user.following.add(targ_user)
        print(myfollowinglist)
        return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
                                                        "user_posts":user_posts,"user_posts_count":user_posts_count,
                                                        "no_of_following":no_of_following,"followerslist": followerslist,
                                                        "no_of_followers":no_of_followers, "myfollowinglist":myfollowinglist,
                                                        "message":message})


    if request.method=="POST" and "unfollow" in request.POST:
        current_user.following.remove(targ_user)

        print(myfollowinglist)
        return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
                                                        "user_posts":user_posts,"user_posts_count":user_posts_count,
                                                        "no_of_following":no_of_following,"followerslist": followerslist,
                                                        "no_of_followers":no_of_followers, "myfollowinglist":myfollowinglist,
                                                        "message":message})


    else:
        return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
                                                        "user_posts":user_posts,"user_posts_count":user_posts_count,
                                                        "no_of_following":no_of_following,"followerslist": followerslist,
                                                        "no_of_followers":no_of_followers, "myfollowinglist":myfollowinglist,
                                                        "message":message})






