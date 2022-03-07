from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.db.models import Max,Count
from django.core.exceptions import ObjectDoesNotExist
from .forms import RouteForm
from .models import User, Route, Comment
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
            return render(request, "Capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Capstone/register.html")
@login_required
def passenger(request):
    current_user = request.user

    all_routes=Route.objects.all().order_by('-created_date')
    page = paging(request, all_routes)
    routes_count = all_routes.count()





    comments = Comment.objects.order_by('-created_date')



    if request.method == "POST" and "route_reply" in request.POST:
        comm_txt = request.POST["comm_txt"]
        route_id = request.POST.get("route_id")

        comment(request,comm_txt,route_id)

        return render(request, "Capstone/passenger.html", {"all_routes": all_routes,
                                                           "comments": comments,"count":page.count,"page":page})

    return render(request, "Capstone/passenger.html", {"all_routes": all_routes,"count": page.count, "page": page,
                                                       'routes_count':routes_count})

@login_required
def driver(request):

    form = RouteForm

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RouteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            created_date = timezone.now()
            origin=request.POST["departure"]
            destination = request.POST["destination"]
            date_orig = request.POST["date_orig"]
            time_orig = request.POST["time_orig"]
            time_dep = request.POST["time_dep"]
            cost= request.POST["cost"]
            no_pass = request.POST["no_pass"]
            map_pic=request.POST['map_pic']
            #print(form)
            form=RouteForm
            msg="Trip created successfully!"


            create_route(request,origin,destination,date_orig,time_orig,time_dep,cost,no_pass,map_pic,created_date)



            # redirect to a new URL:
            return render(request, 'Capstone/driver.html', {'msg': msg,'form':form})
        else:
            #print(form.errors)
            return render(request, 'Capstone/driver.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RouteForm



    return render(request, 'Capstone/driver.html',{'form': form})


def bing(request):
    return render(request, "Capstone/bing.html")



def create_route(request,origin,destination,date_orig,time_orig,time_dep,cost,no_pass,map_pic,created_date):
    thedriver=request.user






    myroute = Route.objects.create_route(origin=origin,destination=destination,date_orig=date_orig,
                                         time_orig=time_orig,time_dep=time_dep,cost=cost, no_pass=no_pass,
                                         thedriver=thedriver,map_pic=map_pic,created_date=created_date)

    return HttpResponseRedirect(reverse("index"))
@login_required
def profile(request, user_id):

    current_user = request.user
    targ_user = User.objects.get(id=user_id)
    user_routes=Route.objects.filter(thedriver_id=user_id).order_by('-created_date')
    page = paging(request, user_routes)
    user_routes_count=user_routes.count()

    # myfollowinglist = current_user.followers.all()
    # followinglist=targ_user.followers.all()
    # followerslist=User.objects.filter(followers=user_id)
    # no_of_followers=len(followerslist)
    # no_of_following=len(followinglist)
    # print(current_user,"Your followers are", followerslist)
    # print(current_user,"You r following",myfollowinglist)
    if request.method == "POST" and "post_reply" in request.POST:
        reply_txt = request.POST["reply_txt"]
        mypost_reply = request.POST.get("post_id")
        #reply(request, reply_txt, mypost_reply)
        return render(request, "Capstone/profile.html", {"targ_user": targ_user})

    if request.method == "POST" and "load_route" in request.POST:

        route_to_load_id = request.POST.get("route_to_load_id")
        #edit_post(request,post_to_load_id)
        route_to_load = Route.objects.get(pk=route_to_load_id)



        return render(request, "Capstone/edit_route.html", {"route_to_load": route_to_load})
    # if targ_user in followinglist:
    #     print(request.user,"you are following user", targ_user)
    #

    #created_date = timezone.now()

    # creating pages


    # if request.method=="POST" and "follow" in request.POST:
    #     targ_user.following.add(current_user)
    #     followerslist = User.objects.filter(followers=user_id)
    #     no_of_followers = len(followerslist)
    #     #print(current_user,"Now you are following", myfollowinglist)
    #     print(targ_user, "has these followers", followerslist)
    #     return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
    #                                                     "user_posts":user_routes,"user_posts_count":user_routes_count,
    #                                                     "no_of_following":no_of_following,"followerslist": followerslist,
    #                                                     "no_of_followers":no_of_followers,
    #                                                     "myfollowinglist":myfollowinglist})

    #
    # if request.method=="POST" and "unfollow" in request.POST:
    #     targ_user.following.remove(current_user)
    #     followerslist = User.objects.filter(followers=user_id)
    #     no_of_followers = len(followerslist)
    #
    #     print(current_user,"Now you are following", myfollowinglist)
    #     print(targ_user, "has these followers", followerslist)
    #     return render(request, "network/profile.html", {"targ_user": targ_user, "followinglist": followinglist,
    #                                                     "user_posts":user_routes,"user_posts_count":user_routes_count,
    #                                                     "no_of_following":no_of_following,"followerslist": followerslist,
    #                                                     "no_of_followers":no_of_followers, "myfollowinglist":myfollowinglist})


    else:

        return render(request, "Capstone/profile.html", {"targ_user": targ_user,"count":page.count,"page":page ,'user_routes_count':user_routes_count})

def paging(request,the_posts):
    # creating pages
    post_paginator=Paginator(the_posts,10)

    page_num = request.GET.get("page")
    return post_paginator.get_page(page_num)


def edit_route(request, route_id):

    route_to_load = Route.objects.get(pk=route_id)
    if request.user == route_to_load.thedriver:
        if request.method =="POST" and "edit_route" in request.POST:

            edit_txt = request.POST["edit_txt"]
            route_to_load.description=edit_txt
            route_to_load.save()

            return HttpResponseRedirect(reverse("index"))
        if request.method == "POST" and "del_post" in request.POST:
            route_to_load.delete()
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "Capstone/edit_route.html",{"route_to_load":route_to_load})
    else:
        return render(request, "network/errors/invalid.html")

@csrf_exempt
@login_required
def join_route(request,route_id):

    # Query for requested route
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "Trip not found."}, status=404)

    # Return post contents
    if request.method == "POST":
        route = Route.objects.get(id=route_id)
        route.thepassenger.add(request.user)
        print("joined trip no ", route.id)

        return JsonResponse({"message": "Trip joined successfully."}, status=201)


    return JsonResponse({"error": "POST request required."}, status=400)

@csrf_exempt
@login_required
def leave_route(request,route_id):

    # Query for requested post
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "Trip not found."}, status=404)

    # Return post contents
    if request.method == "POST":
        route = Route.objects.get(id=route_id)
        route.thepassenger.remove(request.user)
        print("You left trip no ",route.id)

        return JsonResponse({"message": "You left trip successfully."}, status=201)


    return JsonResponse({"error": "POST request required."}, status=400)


def comment(request,comm_txt,route_id):

    route_comm = Route.objects.get(id=route_id)
    created_date = timezone.now()
    owner = request.user

    #route_comm = Comment.objects.filter(route_comm=route.id)
    #print(route_comm)
    comment = Comment.objects.create_comment(comm_txt=comm_txt, created_date=created_date, owner=owner,
                                       route_comm=route_comm)
    comment.save()
    #print(comment)
    comment.lists.add(route_comm)
    return HttpResponseRedirect(reverse("index"))