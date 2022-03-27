

   document.addEventListener('DOMContentLoaded', function() {

       var sortbtn = document.querySelector('#sortbtn');
        sortbtn.addEventListener('click', sort);
        // checking if current passengers >= max passengers so changing Join btn to Closed
        document.querySelectorAll('.joinleave').forEach((element) => {
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

            }
        }
        )





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
            console.log(route_id);
            console.log(max_pass);


// checking if current passengers >= max passengers so not allowing joinining but only leaving
       if (no_pass < max_pass){

            if(element.title == "Join")
            {


                element.style.color = "#B22222";
                element.style.border = "1px solid #B22222";
                element.title="Leave";
                element.innerHTML="Leave";
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML++;
                join_route(route_id);
                est_cost(route_id);

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





       else {
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

                }

               }



        })
    }});

    function sort(){
    alert('sorting')
    document.querySelectorAll('#route').forEach((element) => {


    var fin=element.dataset.fin;
    var fin_set = route['fin_set'];
    console.log(document.querySelector(".media").style.display);
    console.log(fin)
     console.log(fin_set)
     alert('sorting')





       if (fin == 'True' || fin_set=="True") {document.querySelector('.media').style.display='none';

       }
       else{document.querySelector('.media').style.display='block';

       }
})}


 function join_route(route_id)
{
    fetch(`/join/route/${route_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
function leave_route(route_id)
{
    fetch(`/leave/route/${route_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
    }


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
       console.log('the max passengers are', max_pass);
       console.log(init_cost);
       var no_passengers= parseFloat(document.querySelector(`#thepassengercounter_${route_id}`).innerHTML);

       console.log(no_passengers);
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



   })

