
   document.querySelectorAll('.joinleave').forEach((element) => {
        element.onclick = () => {



            var route_id = element.dataset.id;


            console.log(route_id)
            if(element.title == "Join")
            {


                element.style.color = "#B22222";
                element.style.border = "1px solid #B22222";
                element.title="Leave"
                element.innerHTML="Leave"
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML++;
                join_route(route_id);
            }
            else if (element.title == "Leave")
            {   console.log(element)

                element.title="Join"
                element.innerHTML="Join"
                element.style.color = "#228B22";
                element.style.border = "1px solid  #228B22";
                document.querySelector(`#thepassengercounter_${route_id}`).innerHTML--;
                leave_route(route_id);
            }
        }
    });
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