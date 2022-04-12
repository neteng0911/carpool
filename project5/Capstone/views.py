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



from django.core.exceptions import ObjectDoesNotExist
from qr_code.qrcode.utils import MeCard

from .forms import RouteForm
from .models import User, Route, Comment, Message, Qrcode


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
        name = request.POST["name"]
        surname = request.POST["surname"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, name=name,surname=surname)
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
    exp_cost = 0

    all_routes = Route.objects.all().order_by('-created_date')
    page = paging(request, all_routes) #paging
    routes_count = all_routes.count()

    comments = Comment.objects.order_by('-created_date')  #comments on trips

    # for ro in all_routes:
    #     if ro.thepassenger.all().count()==0:
    #         exp_cost=ro.cost
    #     else:
    #         exp_cost=ro.cost/ro.thepassenger.all().count()
    #     return exp_cost





    if request.method == "POST" and "route_reply" in request.POST:
        comm_txt = request.POST["comm_txt"]
        route_id = request.POST.get("route_id")

        comment(request, comm_txt, route_id)

        return render(request, "Capstone/passenger.html", {"all_routes": all_routes,
                                                           "comments": comments, "count": page.count, "page": page,
                                                           'routes_count': routes_count})
    if request.method == "GET" and "load_route" in request.POST:
        return render(request, 'Capstone/route.html')



    return render(request, "Capstone/passenger.html", {"all_routes": all_routes,
                                                       "comments": comments, "count": page.count, "page": page,
                                                       'routes_count': routes_count})


@login_required
def driver(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RouteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            created_date = timezone.now()
            departure = request.POST["departure"]
            destination = request.POST["destination"]
            date_orig = request.POST["date_orig"]
            time_orig = request.POST["time_orig"]
            time_dep = request.POST["time_dep"]
            cost = request.POST["cost"]
            no_pass = request.POST["no_pass"]
            map_pic = request.POST['map_pic']
            # print(form)
            form = RouteForm
            msg = "Trip created successfully!"

            create_route(request, departure, destination, date_orig, time_orig, time_dep, cost, no_pass, map_pic,
                         created_date)

            # redirect to a new URL:
            return render(request, 'Capstone/driver.html', {'msg': msg, 'form': form})
        else:
            # print(form.errors)
            return render(request, 'Capstone/driver.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RouteForm

    return render(request, 'Capstone/driver.html', {'form': form})

#test bing api
def bing(request):
    return render(request, "Capstone/bing.html")


def create_route(request, departure, destination, date_orig, time_orig, time_dep, cost, no_pass, map_pic, created_date):
    thedriver = request.user

    myroute = Route.objects.create_route(departure=departure, destination=destination, date_orig=date_orig,
                                         time_orig=time_orig, time_dep=time_dep, cost=cost, no_pass=no_pass,
                                         thedriver=thedriver, map_pic=map_pic, created_date=created_date)

    return HttpResponseRedirect(reverse("index"))

# visit user's profile
@login_required
def profile(request, user_id):
    current_user = request.user
    targ_user = User.objects.get(id=user_id)
    qr_codes = []
    qrcodes=[]

    user_routes = Route.objects.filter(thedriver_id=user_id).order_by('-created_date')
    page = paging(request, user_routes)
    user_routes_count = user_routes.count()
    user_messages = current_user.messages.all()
    fin_trips = []




    qrroute = Route.objects.get(pk=request.GET.get('route_to_load_id'))
    qr_codes = Qrcode.objects.filter(trip=qrroute)

    # for route in user_routes:
    #
    #
    #     if route.fin() == True or route.fin_set == True:
    #         fin_trips.append(route)
    #
    #         for trip in fin_trips:
    #             qr_codes = Qrcode.objects.filter(trip=trip)

    #             for r in qrcodes:
    #
    #                 #print(route.id, r.code)
    #                 qr_codes.append(r.code)
    # print(qr_codes)








    # for route in user_routes:
    #     a=route.thepassenger.all()
    #     for i in a:
    #         b=i.username
    #         print(b)


    user_passenger_list = current_user.thepassengers.all()
    user_passenger_count = user_passenger_list.count()
    #
    # print (user_passenger_list, user_passenger_count)
    # print('******************')



    comments = Comment.objects.order_by('-created_date')

    if request.method == "POST" and "route_reply" in request.POST:
        comm_txt = request.POST["comm_txt"]
        route_id = request.POST.get("route_id")

        comment(request, comm_txt, route_id)
        return render(request, "Capstone/profile.html", {"targ_user": targ_user,'comments':comments,
                                                         'user_routes':user_routes,'page':page,
                                                         'user_routes_count': user_routes_count,'user_passenger_list':user_passenger_list, 'user_passenger_count':user_passenger_count})

    if request.method == "POST" and "load_route" in request.POST:
        route_to_load_id = request.POST.get("route_to_load_id")

        route_to_load = Route.objects.get(pk=route_to_load_id)

        edit_route(request, route_to_load_id)

        return render(request, "Capstone/edit_route.html", {"route_to_load": route_to_load})

    if request.method == "POST" and "finalise_trip" in request.POST:
        route_to_load_id = request.POST.get("route_to_load_id")

        route_to_load = Route.objects.get(pk=route_to_load_id)
        route_to_load.fin_set=True
        message_cl="Passenger list completed"
        print(message_cl)

        route_to_load.save()
        return render(request, "Capstone/profile.html", {"targ_user": targ_user, "count": page.count, "page": page,
                                                         'user_routes_count': user_routes_count,'message_cl':message_cl
                                                         ,'user_passenger_list':user_passenger_list, 'user_passenger_count':user_passenger_count})

    else:

        return render(request, "Capstone/profile.html", {"targ_user": targ_user, "count": page.count, "page": page,
                                                         'user_routes_count': user_routes_count,
                      'user_passenger_list':user_passenger_list, 'user_passenger_count':user_passenger_count, 'user_messages':user_messages,'qr_codes':qr_codes})


def paging(request, the_posts):
    # creating pages
    post_paginator = Paginator(the_posts, 10)

    page_num = request.GET.get("page")
    return post_paginator.get_page(page_num)


@login_required
def edit_route(request, route_id):
   # alert = 1
    route = Route.objects.get(pk=route_id)

    # form = RouteForm()

    if request.user == route.thedriver:
        # if request.method=='GET':
        #     form = RouteForm(instance=route)
        #
        #     return render(request, "Capstone/edit_route.html", {"route": route, 'form': form})

        if request.method == "POST" and "edit_route" in request.POST:
            form = RouteForm(request.POST, instance=route)

            route.departure = request.POST["departure"]
            route.destination = request.POST["destination"]
            route.date_orig = request.POST["date_orig"]
            route.time_orig = request.POST["time_orig"]
            route.time_dep = request.POST["time_dep"]
            route.cost = request.POST["cost"]
            route.no_pass = request.POST["no_pass"]
            route.map_pic = request.POST['map_pic']
            msg = "Trip edited successfully!"
            if form.is_valid():
                # alert = 1
                # print(alert)


                route.save()
                # messages.success(request, 'Trip edited succesfully')
                return render(request, "Capstone/edit_route.html", {"route": route, 'form': form, 'msg':msg})
                #return HttpResponseRedirect(reverse("index"))

            else:
                form = RouteForm(instance=route)
                msger = "Invalid Input please try again"
                # alert = 0
                # print(alert)
                # messages.error(request, 'Invalid form submission.')
                # messages.error(request, form.errors)

                return render(request, "Capstone/edit_route.html", {"route": route, 'form': form, 'msger':msger})

        if request.method == "POST" and "del_route" in request.POST:
            route.delete()
            return HttpResponseRedirect(reverse("index"))

        else:
            form = RouteForm(instance=route)

            return render(request, "Capstone/edit_route.html", {"route": route, 'form':form})
    else:
        return render(request, "Capstone/errors/invalid.html")


@csrf_exempt
@login_required
def join_route(request, route_id):
    # Query for requested route
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "Trip not found."}, status=404)

    # Return post contents
    if request.method == "POST":
        route = Route.objects.get(id=route_id)
        route.thepassenger.add(request.user)
        qrcode=Qrcode(passenger=request.user, trip=route)
        qrcode.save()

        print(request.user, "joined trip no ", route.id)

        return JsonResponse({"message": "Trip joined successfully."}, status=201)

    return JsonResponse({"error": "POST request required."}, status=400)


@csrf_exempt
@login_required
def leave_route(request, route_id):
    # Query for requested post
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "Trip not found."}, status=404)

    # Return post contents
    if request.method == "POST":
        route = Route.objects.get(id=route_id)
        route.thepassenger.remove(request.user)
        Qrcode.objects.get(passenger=request.user, trip=route).delete()
        print("You left trip no ", route.id)

        return JsonResponse({"message": "You left trip successfully."}, status=201)

    return JsonResponse({"error": "POST request required."}, status=400)


def comment(request, comm_txt, route_id):
    route_comm = Route.objects.get(id=route_id)
    created_date = timezone.now()
    owner = request.user

    # route_comm = Comment.objects.filter(route_comm=route.id)
    # print(route_comm)
    comment = Comment.objects.create_comment(comm_txt=comm_txt, created_date=created_date, owner=owner,
                                             route_comm=route_comm)
    comment.save()
    # print(comment)
    comment.lists.add(route_comm)
    return HttpResponseRedirect(reverse("index"))

# load route in json format
@login_required
def load_route(request, route_id):

    try:
        route = Route.objects.get(pk=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "Route not found."}, status=404)


    if request.method == "GET":
        return JsonResponse(route.serialize())
    return render(request, "Capstone/route.html", {"route": route})

# load route in web view
@login_required
def webload_route(request, route_id):

    try:
        route = Route.objects.get(pk=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "Route not found."}, status=404)
    passengers = route.thepassenger.all()
    # reply comments
    if request.method == "GET":
        #qrcode = Qrcode.objects.get(trip=route, passenger=request.user)
        # print('qrcode ', qrcode.code)

        return render(request, "Capstone/route.html", {"route": route, 'passengers':passengers})

    comments = Comment.objects.order_by('-created_date')
    route = Route.objects.get(pk=route_id)
    qrcode = Qrcode.objects.get(trip=route, passenger=request.user)




    if request.method == 'POST' and 'remove' in request.POST:
        passenger_id = int(request.POST['passenger'])
        remove_passenger(request, route_id,passenger_id)
        return render(request, "Capstone/route.html", {"route": route,
                                                           "comments": comments, 'passengers':passengers})


    if request.method == "POST" and "route_reply" in request.POST:
        comm_txt = request.POST["reply_txt"]


        comment(request, comm_txt, route_id)

        return render(request, "Capstone/route.html", {"route": route,
                                                           "comments": comments, 'passengers':passengers})
    if request.method == "POST" and "edit_route" in request.POST:


        return render(request, "Capstone/route.html", {"route": route, 'passengers':passengers})
    return render(request, "Capstone/route.html", {"route": route, 'passengers':passengers, 'qrcode':qrcode})
# load trips that are not Closed either by date or by user or by not available seats
@login_required
def find_valid_trips(request):

    valid_trips = []
    fin_routes = Route.objects.filter(fin_set=False).order_by('-created_date')
    comments = Comment.objects.order_by('-created_date')
    for route in fin_routes:

        if route.fin() == False:
            valid_trips.append(route)

    print('valid trips', valid_trips)
    routes_count = len(valid_trips)
    page_valid_trips = paging(request, valid_trips)

    return render(request, "Capstone/validtrips.html", {"all_routes": valid_trips,
                                                        "comments": comments, "count": page_valid_trips.count,
                                                        "page": page_valid_trips,
                                                        'routes_count': routes_count})

@login_required
def remove_passenger(request, route_id, passenger_id):
    route = Route.objects.get(pk=route_id)
    passenger = User.objects.get(pk=passenger_id)
    created_date = timezone.now()



    route.thepassenger.remove(passenger)
    #Qrcode.objects.filter(passenger=passenger,trip=route).delete()
    content = 'You have been removed from route'
    message = Message(content=content, created_date=created_date, route_id=route_id)
    message.save()
    # print(comment)
    message.recipient.add(passenger)


    print('passenger',passenger, 'removed from route', route_id)
