from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
#from cookie_consent.util import get_cookie_value_from_request
from django.db.models import Q
import datetime
from django.utils.timezone import now, make_aware
from datetime import date
from django.utils import timezone
from datetime import date, datetime
from django.utils.timezone import make_aware




from .forms import RouteForm, UserForm
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
        dob = request.POST['dob']
        birthday=datetime.datetime.strptime(dob,'%Y-%m-%d')

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if User.objects.filter(username=username).exists():
            return render(request, "Capstone/register.html", {
                "message": "Username already exists."
            })
        if User.objects.filter(email=email).exists():
            return render(request, "Capstone/register.html", {
                "message": "Email exists."
            })
        if password != confirmation:
            return render(request, "Capstone/register.html", {
                "message": "Passwords must match."
            })




        if datetime.datetime.today() - birthday < datetime.timedelta(days=18 * 365):
            return render(request, "Capstone/register.html", {
                "message": "You must be over 18 years old to register"
            })


        # Attempt to create new user

        user = User.objects.create_user(username, email, password, name=name,surname=surname)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your Carpooling registration'
        message = render_to_string('Capstone/acc_activate_email.html',{'user':user,'domain':current_site.domain,'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                                                  'token':account_activation_token.make_token(user)})
        to_email = email
        email = EmailMessage(mail_subject,message,to=[to_email])
        email.send()
        return render(request, 'Capstone/confirm_email.html',{'user':user})
        #return HttpResponse('Please confirm your email address to complete registration')






        #login(request, user)
        #return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Capstone/register.html")

def activate (request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'Capstone/confirm_email_success.html', {'user': user})
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
@login_required(login_url='login')
def passenger(request):
    current_user = request.user
    exp_cost = 0
    time_now=datetime.now().time()
    #print(time_now)
    #print(datetime.now().timestamp())
    #print(datetime.now().date().strftime("%Y-%m-%d"))
    all_routes = Route.objects.all().order_by('-created_date')
    page = paging(request, all_routes) #paging
    routes_count = all_routes.count()

    comments = Comment.objects.order_by('-created_date')  #comments on trips

    # for ro in all_routes:
    #     print(ro.date_orig, 'vs', datetime.now().date().strftime("%Y-%m-%d"))
    #
    #     if ro.date_orig == datetime.now().date().strftime("%Y-%m-%d"):
    #         print(ro.id, 'equal')
    #     else:
    #         print(ro.id, 'not equal')



    if request.method=='POST' and 'searched' in request.POST:
        searched=request.POST['searched']
        if searched =='':
            message ='Please enter a valid search'
            return render(request, "Capstone/searchedtrips.html", {"message":message})
        else:
            searched_routes = Route.objects.filter(Q(departure__icontains=searched) | Q(destination__icontains=searched)).order_by('-created_date')
            #print('you searched for ',searched)
            #print(searched_routes)
            comments = Comment.objects.order_by('-created_date')
            page_searched_routes = paging(request, searched_routes)
            searched_routes_count=searched_routes.count()

            return render(request, "Capstone/searchedtrips.html", {"all_routes": searched_routes,
                                                                   "comments": comments,
                                                                   "count": page_searched_routes.count,
                                                                   "page": page_searched_routes,
                                                                    "searched":searched,
                          "searched_routes_count":searched_routes_count})


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
                                                       'routes_count': routes_count,'time_now':time_now})


@login_required(login_url='login')
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
            date_orig_str = request.POST["date_orig"]
            time_orig = request.POST["time_orig"]
            time_dep = request.POST["time_dep"]
            cost = request.POST["cost"]
            no_pass = request.POST["no_pass"]
            map_pic = request.POST['map_pic']
            dist = request.POST['dist']
            #d_a = request.POST['d_a']
            #print(form)
            form = RouteForm
            msg = "Trip created successfully!"
            date_orig=datetime.strptime(date_orig_str,"%Y-%m-%d")
            create_route(request, departure, destination, date_orig, time_orig, time_dep, cost, no_pass, map_pic,
                         created_date,dist)

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


def create_route(request, departure, destination, date_orig, time_orig, time_dep, cost, no_pass, map_pic, created_date, dist):
    thedriver = request.user

    myroute = Route.objects.create_route(departure=departure, destination=destination, date_orig=date_orig,
                                         time_orig=time_orig, time_dep=time_dep, cost=cost, no_pass=no_pass,
                                         thedriver=thedriver, map_pic=map_pic, created_date=created_date,dist=dist)

    return HttpResponseRedirect(reverse("index"))

# visit user's profile
@login_required
def profile(request, user_id):
    current_user = request.user
    targ_user = User.objects.get(id=user_id)


    user_routes = Route.objects.filter(thedriver_id=user_id).order_by('-created_date')
    page = paging(request, user_routes)
    user_routes_count = user_routes.count()
    user_messages = current_user.messages.all()
    user_passenger_list = current_user.thepassengers.all()
    user_passenger_count = user_passenger_list.count()


    if request.method == "POST" and "edit_profile" in request.POST:

        edit_profile(request,request.user_id)




        return render(request, "Capstone/edit_profile.html")

    #qrroute = Route.objects.get(pk=request.GET.get('route_to_load_id'))
    for r in user_routes:
        #print(r)
        mycode = r.qrcodes.all()

        for t in mycode:
            passen = t.passenger
            print(passen)






    comments = Comment.objects.order_by('-created_date')

    if request.method == "POST" and "route_reply" in request.POST:
        comm_txt = request.POST["comm_txt"]
        route_id = request.POST.get("route_id")

        comment(request, comm_txt, route_id)
        return render(request, "Capstone/profile.html", {"targ_user": targ_user,'comments':comments,
                                                         'user_routes':user_routes,'page':page,
                                                         'user_routes_count': user_routes_count,
                                                         'user_passenger_list':user_passenger_list, 'user_passenger_count':user_passenger_count})

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
        #print(message_cl)

        route_to_load.save()
        return render(request, "Capstone/profile.html", {"targ_user": targ_user, "count": page.count, "page": page,
                                                         'user_routes_count': user_routes_count,'message_cl':message_cl
                                                         ,'user_passenger_list':user_passenger_list, 'user_passenger_count':user_passenger_count})

    else:

        return render(request, "Capstone/profile.html", {"targ_user": targ_user, "count": page.count, "page": page,
                                                         'user_routes_count': user_routes_count,
                      'user_passenger_list':user_passenger_list, 'user_passenger_count':user_passenger_count,
                                                         'user_messages':user_messages})
@login_required
def edit_profile(request, user_id):
    current_user = request.user
    targ_user = User.objects.get(id=user_id)
    if request.method=='GET':
        form = UserForm(request.POST, request.FILES, instance=current_user)
        return render(request, "Capstone/edit_profile.html", {'form': form, "targ_user": targ_user,})


    if request.method == "POST" and "Update" in request.POST:
        form = UserForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid:
            form.save()
            messages.success(request, "profile successfully updated")


            return render(request, "Capstone/edit_profile.html", {'form': form, "targ_user": targ_user,})


def paging(request, the_posts):
    # creating pages
    post_paginator = Paginator(the_posts, 10)

    page_num = request.GET.get("page")
    return post_paginator.get_page(page_num)


@login_required
def edit_route(request, route_id):

    route = Route.objects.get(pk=route_id)
    passengers = route.thepassenger.all()


    if request.user == route.thedriver:


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
            route.d_a = request.POST['d_a']
            msg = "Trip edited successfully!"
            if form.is_valid():



                route.save()

                for p in passengers:
                    content = 'Attention! Driver just edited the trip'
                    created_date = timezone.now()
                    message = Message(content=content, created_date=created_date, route_id=route_id)
                    message.save()
                    # print(comment)
                    message.recipient.add(p)

                return render(request, "Capstone/edit_route.html", {"route": route, 'form': form, 'msg':msg})


            else:
                form = RouteForm(instance=route) #instance loads the pre-filled form
                msger = "Invalid Input please try again"


                return render(request, "Capstone/edit_route.html", {"route": route, 'form': form, 'msger':msger})

        if request.method == "POST" and "del_route" in request.POST:



            for p in passengers:
                content = 'Attention! Driver just cancelled the trip'
                created_date = timezone.now()
                message = Message(content=content, created_date=created_date, route_id=route_id)
                message.save()
                # print(comment)
                message.recipient.add(p)
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
        #qrcode=Qrcode(passenger=request.user, trip=route)
        qrcode = Qrcode(passenger=request.user)
        qrcode.save()
        qrcode.trip.add(route)

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
        return JsonResponse({"error": "Trip not found."}, status=404)


    if request.method == "GET":
        return JsonResponse(route.serialize())
    return render(request, "Capstone/route.html", {"route": route})

# load route in web view
@login_required
def webload_route(request, route_id):

    try:
        route = Route.objects.get(pk=route_id)
    except Route.DoesNotExist:
        return JsonResponse({"error": "trip not found."}, status=404)
    passengers = route.thepassenger.all()
    # reply comments
    if request.method == "GET":

        if passenger == request.user:
            trip = Route.objects.get(pk=route_id)
            #codes = trip.qrcodes.all()

            myqr = trip.qrcodes.get(passenger= request.user)
            mycode = myqr.code
            #print(myqr)
            return render(request, "Capstone/route.html", {"route": route, 'passengers': passengers, 'mycode': mycode})
        else:
            trip = Route.objects.get(pk=route_id)

            mycodes=trip.qrcodes.all()
            #print(mycodes)
            for my in mycodes:
                mycode = my.code

                #print(my.code)



                return render(request, "Capstone/route.html", {"route": route, 'passengers':passengers,'mycode':mycode})

    comments = Comment.objects.order_by('-created_date')





    if request.method == 'POST' and 'remove' in request.POST:
        passenger_id = int(request.POST['passenger'])
        remove_passenger(request, route_id,passenger_id)
        return render(request, "Capstone/route.html", {"route": route,
                                                           "comments": comments, 'passengers':passengers})


    if request.method == "POST" and "route_reply" in request.POST:
        comm_txt = request.POST["comm_txt"]


        comment(request, comm_txt, route_id)

        return render(request, "Capstone/route.html", {"route": route,
                                                           "comments": comments, 'passengers':passengers})
    if request.method == "POST" and "edit_route" in request.POST:


        return render(request, "Capstone/route.html", {"route": route, 'passengers':passengers})
    return render(request, "Capstone/route.html", {"route": route, 'passengers':passengers})
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
    Qrcode.objects.filter(passenger=passenger,trip=route).delete()
    content = 'Attention! You have been removed from trip'
    message = Message(content=content, created_date=created_date, route_id=route_id)
    message.save()
    # print(comment)
    message.recipient.add(passenger)


    print('passenger',passenger, 'removed from route', route_id)

def terms(request):
    return render(request, "Capstone/terms.html")



# def myview(request, *args, **kwargs):
#   cc = get_cookie_value_from_request(request, "mycookies")
#   if cc:
#     # add cookie
#     cc = get_cookie_value_from_request(request, "mycookies", "mycookie1")

