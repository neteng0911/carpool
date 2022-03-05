

        let mp=localStorage.getItem('mp');
        document.getElementById("map").src = mp;
        const today= new Date();


document.addEventListener('DOMContentLoaded', function() {

        document.querySelector('#sub_route').style.display = 'block';
        document.querySelector('#map').style.display = 'block';
        document.querySelector('#map_pl').style.display = 'block';
        document.querySelectorAll('#sear').forEach((element) => {
        element.onclick = () => search_route();
        const form=document.getElementById("addresses");
        const date=form.elements["date_orig"];
        const time_orig=form.elements["time_orig"];
        const time_dep=form.elements["time_dep"];
        date.addEventListener('input', validateform);




})
})
function search_route(){
         const form=document.getElementById("addresses");
         const start=form.elements["dep"];
         const end=form.elements["dest"];
         if (start.value.trim() === "" || end.value.trim() === "" ){




         }  else    {


         <!--'Ymhttou%2072%20Athens'-->
         <!--'Skoufa%202%20Athens'-->

         'https://dev.virtualearth.net/REST/v1/Imagery/Map/imagerySet/centerPoint/zoomLevel/Routes/\
         travelMode?waypoint.1={routeWaypoint1}&waypoint.2={routeWaypoint2}\
         &waypoint.n={routeWaypointn}&mapSize={mapSize}\
         &avoid={avoidOptions}&pushpin={pushpin}&timeType={timetType}&dateTime={dateTime}\
         &maxSolutions={maxSolutions}\
         &distanceBeforeFirstTurn={distanceBeforeFirstTurn}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&&o=json&key='
         let key='Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF'
         let route=`https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=${start.value}1&wp.1=${end.value}2&o=json&key=`
         let point='https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/Solonos%20Athens?zoomlevel=20&mapLayer=TrafficFlow&o=json&key='
         let place='Ymhttoy%72%20Athens'

         let test=`https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/${place}?mapLayer=TrafficFlow&o=json&key=`


         localStorage.setItem("mp",route+key );


        let data = fetch(mp)

           .then(response=>{
           if (response.status==200){

        document.querySelector('#addresses').style.display = 'none';
        document.querySelector('#sub_route').style.display = 'block';
        document.querySelector('#map').style.display = 'block';
        document.querySelector('#map_pl').style.display = 'block';
        document.getElementById("map").src = mp;
        document.getElementById("id_departure").value = start.value;
        document.getElementById("id_destination").value = end.value;





         }
         else{

alert("address not found");

         }})
         .then(response => console.log("res: ", response))





         .catch(err => console.log("err: ", err));

         console.log(data)


        }
        }




function subm_route(){
        let mp=localStorage.getItem('mp');
        let data = fetch(mp)

           .then(response=>{
       
       document.getElementById("map").src = mp;


        document.querySelector('#addresses').style.display = 'block';
        document.querySelector('#map').style.display = 'block';
        document.querySelector('#sub_route').style.display = 'block';

})



        }





function validateform(e){

        e.preventDefault();

        const form=document.getElementById("addresses");
        const date=form.elements["date_orig"]
        if (date<today){
        alert('please select a later day')
        date.focus();



        }
        else{
            form.submit();
                }

}


//document.querySelector('form').onsubmit=function()