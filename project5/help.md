# Capstone
## CarPooling

#### This is the final project for CS50’s Web Programming with Python and JavaScript
 ## Index
- ##### Summary
- ##### Instruction on how to use
- ##### Distinctiveness and Complexity
- ##### Files

##### Summary
The app is a carpooling one. It helps commuters to share a vehicle to commute from and to their jobs, in order to reduce CO2 emmisions travel costs and traffic congestion.
The users have the ability to use the app as **Drivers** i.e to create a custom route (from to) on a specific date and time of origin and return, along with the number of available seats and the cost that the passengers will share.
Then the commuters that wish to find a driver with a car browse all the available trips and select the one that suits them by joining the trip and become the **Passengers**.

##### Instruction on how to use
The Driver creates the trip via the Bing Route API, by searching the origin and the destination, and then ,if succesfull, the other necessary fields of the Trip form are being filled.
There is a preview of the Trip on the Bing Map so as the Driver to make sure that the correct places have been imported.
There are several validators to prevent user input errors such as start date or time prior to current, or end time prior to start time.
The commuters that need a drive, browse the available trips (all including the closed ones or the valid ones) and join a trip. They bocome the Passenger.
When the available seats become none, then the trip is ==Closed== by the app and no one else can join the trip.
If a Passenger wishes to leave the trip, then his/hers seat becomes available again and if the trip was closed it bocomes available again. 
In case that the Driver wishes to exclude a certain Passenger from the trip (say a prior bad experience or reputation), he can do that and the seat becomes available again. In that case a message appears on the passenger's profile that informs hm/her about being excluded form the trip.
If the start time of the trip has passed then the trip is autoclosed by the app regardless the available seats.
The Driver can manually close the Trip if he/she wants it.
Should the Driver wishes to edit the Trip, he/she can do that, as well as to delete it. A message appears in all passengers profiles.
All messages older than 7 days are hidden to avoid to much info on screen.
If a trip is ==Closed== then a QR code is being created (a 5digit number) that is unique for a passenger for the specific trip. This is for the driver to identify the valid Passengers for the trip. This code is available only to the Passenger and to the Driver so as to check it. If a Passenger leaves the trip the QR code is deleted.
Moreover any user has the ability to comment on the trips and ask questions to the driver.
#### Distinctiveness and Complexity
The app is not a social app nor an e-shop. It's a rather complex app that incorporates many aspects of user interaction. As stated above there are two distinct roles, the Driver and the Passenger, any user can have both roles for different trips. The available info  to any user depending on his/her role, are different, respecting sensible info that shouldn't be available to anyone. For example, when visiting the profile page, if it's his/her shows all the trips that has the role of driver, plus all the passengers of the trip along with the validating QR codes. When visiting other user's profile can see other info such as email, number of trips as a driver, all the trips as the driver etc. The QR codes are not available, nor the passengers of the trips.
The passengers of each trip is only available  to the driver on the profile or the trip page.
There are many layers of validations both in creating a trip, as stated above, and as a passenger. For example the date and time validation of the trip is being handled by the form itself in the backened. The cost input cannot be less than 0 nor the number of available seats.

For every trip that the passenger has joined, if the driver makes any changes, the passengers get a message in the profile page thats is visible for 7 days.


##### Technical Stuff...
The app incorporates 5 modules with fields as ManyToMany relationships and Foreign Keys. Apart from the User model there are the Route, Comment, Message and Qrcode ones. The Route model has a couple of methods for calculating the time and date of the trip so as to auto close the trip depending on the time and the cost per passenger depending on the initial cost and the number of passengers that have joined the trip at that time and updating the DB.
There is also a serialization method so as to interact with the client side through json format with the javascript files.
The Message module has a Manager with a special method for quering, that returns a queryset of the objects that are les than 7 days old. So the filtering is taking place immediatelly and there is no need for doing in views.
django-qr-code needs to be installed so as the app to be able to generate QR codes
Javascript is used in many ways. 
### Files
- The Bing maps API is being called by the ***`map7.js`*** file that takes the input from the Django RouteForm class in ***`forms.py`*** file and according to the rules of the API, the url is being constructed on the client side. Upon submit a call to the API takes place with the origin and destination places that the Driver has chosen and should the call is succesfull a map is being returned with the best route for the trip between the two places. The map in png format is inserted in the template. Since the call is being made on the client side, the image itself can't be stored on the server side due to security reasons. So only the url is being stored on the DB.
Then the Driver fills the rest of the form with the help of Date and Time widgets as pickers and then (provided the validation is passed) the Trip is created. In case the initial search of the places unsuccesful the Driver can't proceed to the next step of filling the rest of the fields (ie date, time, cost etc). The trip is edited on the same way but the ***`edit_route.js`*** file is slightly different than the ***`map7.js`*** file and helps to prefill the form.
- In order to join or leave the trip without the need to reload the page through a fetch POST call with json (with the help of the serialization method in Route model as stated above). Moreover the cost per passenger is calculated on the client side in parallel with the database update through the aformentioned method. All these are beig done with the  ***`join_leave.js`*** file.
- The use of ***`Bootstrap`*** helps to quickly style the frontend and make the pages responsive for ease of use on mobile phones with the help of a ***`styles.css`*** file.
- There are many templates that help to render the ***`views.py`*** file that handles the backened: 
    - driver.html renders the form that creates the trip.
    - edit_route.html renders the form that edits the trip.
    - index,layout, login and register are standard htmls for a django project.
    - passenger.html renders the browse page as a passenger.
    - route.html renders each trip
    - validtrips.html filters the trips that are not closed. (This could have been done with js as well)
- Other files:
    - In the forms.py file the form of the creation of the trip is created with the validators and the widgets.
    - In the urls.py file the urls for the views are constructed.
 
