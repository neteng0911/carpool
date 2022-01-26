from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from django.core.exceptions import ObjectDoesNotExist

from .models import User, Mypost, Reply



def index(request):
    all_posts=Mypost.objects.order_by('-created_date')


    # creating pages
    page=paging(request,all_posts)


    # for post in all_posts:
    #
    #     print(post.likes.all().count())
    #     print("Post number", post.id,"is liked by",post.likes.all())
    #     if request.user in post.likes.all():
    #         print(request.user,"likes post no",post.id)

    created_date = timezone.now()

    owner = request.user

    replies = Reply.objects.order_by('-created_date')

    # if request.method == "POST" and "like" in request.POST:
    #
    #     mypost_like_id = request.POST.get("post_to_like_id")
    #     like(request,mypost_like_id)
    #
    #
    #     return render(request, "network/index.html", {"all_posts": all_posts, "replies": replies,
    #                                                   "count":page.count,"page":page})
    #
    #
    #
    # if request.method == "POST" and "unlike" in request.POST:
    #
    #     mypost_to_unlike_id = request.POST.get("post_to_unlike_id")
    #     unlike(request, mypost_to_unlike_id)
    #
    #
    #     return render(request, "network/index.html", {"all_posts": all_posts,
    #                                                   "replies": replies,"count":page.count,"page":page})

    if request.method == "POST" and "post_reply" in request.POST:
        reply_txt = request.POST["reply_txt"]
        mypost_reply = request.POST.get("post_id")
        reply(request,reply_txt,mypost_reply)
        # mypost = Mypost.objects.get(id=mypost_reply)
        # like_list = mypost.likes.all()
        # my_post_replies = Reply.objects.filter(mypost_reply=mypost_reply)
        # print(my_post_replies)
        # reply = Reply.objects.create_reply(reply_txt=reply_txt, created_date=created_date, owner=owner,
        #                                    mypost_reply=mypost)
        # reply.save()
        # print(reply)
        # reply.lists.add(mypost)
        return render(request, "network/index.html", {"all_posts": all_posts, "replies": replies,"count":page.count,"page":page})




        #here first loads the post in different page before editing it BUT i display it as edit post on the page for the user
    if request.method == "POST" and "load_post" in request.POST:

        post_to_load_id = request.POST.get("post_to_load_id")
        edit_post(request,post_to_load_id)
        post_to_load = Mypost.objects.get(pk=post_to_load_id)



        return render(request, "network/edit_post.html", {"post_to_load": post_to_load})

    else:
        return render(request, "network/index.html",
                      {"all_posts": all_posts, "replies": replies,"count":page.count,"page":page})





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
def following(request):
    myfollowinglist = request.user.followers.all()
    all_posts = Mypost.objects.filter(owner__in=myfollowinglist).order_by('-created_date')
    # creating pages
    page = paging(request, all_posts)
    if request.method == "POST" and "post_reply" in request.POST:
        reply_txt = request.POST["reply_txt"]
        mypost_reply = request.POST.get("post_id")
        reply(request, reply_txt, mypost_reply)


    if request.method == "POST" and "like" in request.POST:

        mypost_like_id = request.POST.get("post_to_like_id")
        like(request,mypost_like_id)

    if request.method == "POST" and "unlike" in request.POST:

        mypost_to_unlike_id = request.POST.get("post_to_unlike_id")
        unlike(request, mypost_to_unlike_id)
    return render(request, "network/following.html",
                  {"all_posts": all_posts,"count":page.count,"page":page})
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
    # return render(request, "network/edit_post.html", {"post_to_load": post_to_load})

#mporei na mhn xreiazetai check!!!!


def edit_post(request, post_id):

    post_to_load = Mypost.objects.get(pk=post_id)
    if request.user == post_to_load.owner:
        if request.method =="POST" and "edit_post" in request.POST:

            edit_txt = request.POST["edit_txt"]
            post_to_load.description=edit_txt
            post_to_load.save()

            return HttpResponseRedirect(reverse("index"))
        if request.method == "POST" and "del_post" in request.POST:
            post_to_load.delete()
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "network/edit_post.html",{"post_to_load":post_to_load})
    else:
        return render(request, "network/errors/invalid.html")

@login_required
def profile(request, user_id):

    current_user = request.user
    targ_user = User.objects.get(id=user_id)
    user_posts=Mypost.objects.filter(owner_id=user_id).order_by('-created_date')
    user_posts_count=user_posts.count()
    page = paging(request, user_posts)
    myfollowinglist = current_user.followers.all()
    followinglist=targ_user.followers.all()
    followerslist=User.objects.filter(followers=user_id)
    no_of_followers=len(followerslist)
    no_of_following=len(followinglist)
    print(current_user,"Your followers are", followerslist)
    print(current_user,"You r following",myfollowinglist)
    if request.method == "POST" and "post_reply" in request.POST:
        reply_txt = request.POST["reply_txt"]
        mypost_reply = request.POST.get("post_id")
        reply(request, reply_txt, mypost_reply)
        return render(request, "network/profile.html", {"targ_user": targ_user,"count":page.count,"page":page})
    if request.method == "POST" and "like" in request.POST:

        mypost_like_id = request.POST.get("post_to_like_id")
        like(request,mypost_like_id)

    if request.method == "POST" and "unlike" in request.POST:

        mypost_to_unlike_id = request.POST.get("post_to_unlike_id")
        unlike(request, mypost_to_unlike_id)

    if targ_user in followinglist:
        print(request.user,"you are following user", targ_user)


    created_date = timezone.now()

    # creating pages
    page = paging(request, user_posts)

    if request.method=="POST" and "follow" in request.POST:
        targ_user.following.add(current_user)
        followerslist = User.objects.filter(followers=user_id)
        no_of_followers = len(followerslist)
        print(current_user,"Now you are following", myfollowinglist)
        print(targ_user, "has these followers", followerslist)
        return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
                                                        "user_posts":user_posts,"user_posts_count":user_posts_count,
                                                        "no_of_following":no_of_following,"followerslist": followerslist,
                                                        "no_of_followers":no_of_followers,
                                                        "myfollowinglist":myfollowinglist,"count":page.count,"page":page})


    if request.method=="POST" and "unfollow" in request.POST:
        targ_user.following.remove(current_user)
        followerslist = User.objects.filter(followers=user_id)
        no_of_followers = len(followerslist)

        print(current_user,"Now you are following", myfollowinglist)
        print(targ_user, "has these followers", followerslist)
        return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
                                                        "user_posts":user_posts,"user_posts_count":user_posts_count,
                                                        "no_of_following":no_of_following,"followerslist": followerslist,
                                                        "no_of_followers":no_of_followers, "myfollowinglist":myfollowinglist,"count":page.count,"page":page})


    else:
        return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
                                                        "user_posts":user_posts,"user_posts_count":user_posts_count,
                                                        "no_of_following":no_of_following,"followerslist": followerslist,
                                                        "no_of_followers":no_of_followers, "myfollowinglist":myfollowinglist,"count":page.count,"page":page})


@csrf_exempt
@login_required
def like_post(request,post_id):

    # Query for requested post
    try:
        mypost = Mypost.objects.get(id=post_id)
    except Mypost.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    # Return post contents
    if request.method == "POST":
        mypost = Mypost.objects.get(id=post_id)
        mypost.likes.add(request.user)
        print("liked post no ", mypost.id)

        return JsonResponse({"message": "Post liked successfully."}, status=201)


    return JsonResponse({"error": "POST request required."}, status=400)

@csrf_exempt
@login_required
def unlike_post(request,post_id):

    # Query for requested post
    try:
        mypost = Mypost.objects.get(id=post_id)
    except Mypost.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    # Return post contents
    if request.method == "POST":
        mypost = Mypost.objects.get(id=post_id)
        mypost.likes.remove(request.user)
        print("unliked post no ",mypost.id)

        return JsonResponse({"message": "Post unliked successfully."}, status=201)


    return JsonResponse({"error": "POST request required."}, status=400)

def reply(request,reply_txt,post_id):

    mypost = Mypost.objects.get(id=post_id)
    created_date = timezone.now()
    owner = request.user

    my_post_replies = Reply.objects.filter(mypost_reply=mypost)
    print(my_post_replies)
    reply = Reply.objects.create_reply(reply_txt=reply_txt, created_date=created_date, owner=owner,
                                       mypost_reply=mypost)
    reply.save()
    print(reply)
    reply.lists.add(mypost)
    return HttpResponseRedirect(reverse("index"))

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def paging(request,the_posts):
    # creating pages
    post_paginator=Paginator(the_posts,10)

    page_num = request.GET.get("page")
    return post_paginator.get_page(page_num)

