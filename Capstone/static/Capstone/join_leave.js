

   document.addEventListener('DOMContentLoaded', function() {
        // get button by id
        //document.getElementById('closedjs_$').style.display='none';
        var trips = document.querySelectorAll('*[id^="closedjs"]');

//        trips = document.querySelectorAll('.closedjs')
         trips.forEach((element) =>{element.style.display='none';})





        // checking if current passengers >= max passengers so changing Join btn to Closed
/*        document.querySelectorAll('.joinleave').forEach((element) => {
            var route_id = element.dataset.id;
            var no_pass= parseFloat(document.querySelector(`#thepassengercounter_${route_id}`).innerHTML);
            var max_pass = parseFloat(document.querySelector(`#max_pass_${route_id}`).innerHTML);

            if (no_pass == max_pass){
                if (element.innerHTML="Join"){


                element.style.color = "#B22222";
                element.style.border = "1px solid #B22222";
                element.title="Closed";
                element.innerHTML="Closed";
                }

            else{

                element.title="Leave";
                element.innerHTML="Leave";
            }
            }

        }
        )*/


//  so as to not reload the page after joining or leaving a trip. It updates the innerHTML instantly
 //and then fetches as POST the route_id json page so as to update the DB



       document.querySelectorAll('.joinleave').forEach((element) => {
            element.onclick = () => {



            var route_id = element.dataset.id;

            fetch(`/route/${route_id}`)

                .then(response => response.json())
                .then(route => {

                if (route.error) {
                    console.log(route.error);
                    alert(route.error)

        }


            var no_pass= parseFloat(document.querySelector(`#thepassengercounter_${route_id}`).innerHTML);
            var max_pass = route["no_pass"];
            var dist = route["dist"];
            var key_num = route["key_num"];
            var co2=dist*2.40*2;
            var fin = document.querySelector(`#fin_${route_id}`).innerHTML;
            var diff_p = max_pass-no_pass


            //console.log(route_id);
            console.log('max passengers  ', max_pass);
            console.log('current passengers ', no_pass);
            console.log('is date passed? ', fin);
            console.log('diff pass ', diff_p);

            //console.log(dist)
            //console.log(key_num)


// checking if current passengers >= max passengers so not allowing joinining but only leaving
       if (no_pass < max_pass){


              if (diff_p==1){
                    if(element.title == "Join")
            {


                element.style.color = "#B22222";
                element.style.border = "1px solid #B22222";
                element.title="Leave";
                element.innerHTML="Leave";
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML++;
                document.querySelector(`#closedjs_${route_id}`).style.display='block';

                alert("Congrats you just saved "+(co2.toFixed(2))+' kg of CO2 by Carpooling')
                join_route(route_id);
                est_cost(route_id);


        }
}


            else if (element.title == "Leave"){
               console.log(element);


                element.title="Join";
                element.innerHTML="Join";
                element.style.color = "#228B22";
                element.style.border = "1px solid  #228B22";
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML--;
                leave_route(route_id);
                est_cost(route_id);

                }}
      else if (no_pass == max_pass){

        if (fin === 'False'){

        if (element.title == "Leave"){
               //console.log(element);


                element.title="Join";
                element.innerHTML="Join";
                element.style.color = "#228B22";
                element.style.border = "1px solid  #228B22";
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML--;
                leave_route(route_id);
                est_cost(route_id);
                document.querySelector(`#closedjs_${route_id}`).style.display='none';
                document.querySelector(`#closed_${route_id}`).style.display='none';


                }










}






/*       else {
                if(element.title == "Closed")
            {
                alert('Sorry, max number of passengers reached');

                element.style.color = "#B22222";
                element.style.border = "1px solid #B22222";
                element.title="Closed";
                element.innerHTML="Closed";
                //document.querySelector(`#thepassengercounter_${route_id}`).innerHTML++;
                //join_route(route_id);
                //est_cost(route_id);

            }*/
/*            else if (element.title == "Leave"){
               console.log(element);


                element.title="Join";
                element.innerHTML="Join";
                element.style.color = "#228B22";
                element.style.border = "1px solid  #228B22";
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML--;
                leave_route(route_id);
                est_cost(route_id);

                }*/

               }



        })

    }})});

   /* function sort(){
    //alert('sorting')
    document.querySelectorAll('.media').forEach((element) => {

    var route_id = element.dataset.id;
    var fin = element.dataset.fin;
    var fin_set = element.dataset.fin_set;
    console.log(route_id, 'style', document.querySelector(".media").style.display);
    console.log(route_id, 'fin', fin);
     console.log(route_id, 'fin_set', fin_set);






       if (fin == 'True' || fin_set=="True") {document.querySelector('.media').style.display='none';

       }
       else{document.querySelector('.media').style.display='block';

       }
})}
*/

 function join_route(route_id)
{
    fetch(`/join/route/${route_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data))


}

function leave_route(route_id)
{
    fetch(`/leave/route/${route_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
    }

// Calculating the cost  per passenger depending on the number of passengers instantly on the page (changing innerHTML)
// The updating of the DB is being done in models by the cost method separately
function est_cost(route_id){


fetch(`/route/${route_id}`)
    .then(response => response.json())
    .then(route => {



        if (route.error) {
            console.log(route.error);
            alert(route.error)

        }

       var origin=route["origin"];
       var destination=route["destination"];
       var init_cost=route["cost"];
       var max_pass=route["no_pass"];
       //console.log('the max passengers are', max_pass);
       //console.log(init_cost);
       var no_passengers= parseFloat(document.querySelector(`#thepassengercounter_${route_id}`).innerHTML);

       //console.log(no_passengers);
       if (no_passengers ===0){
       var cost=init_cost;
       document.querySelector(`#costpp_${route_id}`).innerHTML = cost+'$';
}
       else{
       var cost =init_cost/no_passengers;
       document.querySelector(`#costpp_${route_id}`).innerHTML = cost+'$';


}

    })






    }




