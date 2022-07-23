
// to keep in session last map (not the best implementation
        let mp=sessionStorage.getItem('mp');
        document.getElementById("map").src = mp;

        if (!mp){
        document.querySelector('#map').style.display = 'none';
        document.querySelector('#map_pl').style.display = 'none';

        }
document.addEventListener('DOMContentLoaded', function() {

        document.querySelector('#sub_route').style.display = 'block';
        document.querySelector('#map').style.display = 'block';
        document.querySelector('#map_pl').style.display = 'block';
        document.querySelectorAll('#sear').forEach((element) => {    //searching of the route initially
        element.onclick = () => search_route();
        document.querySelectorAll('#subbtn').forEach((element) => {
        element.onclick = () => subm_route();                       // submitting the route after successful initial search
        const d= new Date();



})
})
function search_route(){
         const form=document.getElementById("addresses");
         const start=form.elements["dep"];
         const end=form.elements["dest"];
         if (start.value.trim() === "" || end.value.trim() === "" ){




         }  else    {


   //      <!--'Ymhttou%2072%20Athens'-->
   //     <!--'Skoufa%202%20Athens'-->

   /*      'https://dev.virtualearth.net/REST/v1/Imagery/Map/imagerySet/centerPoint/zoomLevel/Routes/\
         travelMode?waypoint.1={routeWaypoint1}&waypoint.2={routeWaypoint2}\
         &waypoint.n={routeWaypointn}&mapSize={mapSize}\
         &avoid={avoidOptions}&pushpin={pushpin}&timeType={timetType}&dateTime={dateTime}\
         &maxSolutions={maxSolutions}\
         &distanceBeforeFirstTurn={distanceBeforeFirstTurn}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&&o=json&key=' */
         let key='Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF'  // THIS IS MY BING MAPS API KEY!!!!!!!!!!1
         let route=`https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=${start.value}1&wp.1=${end.value}2&o=json&key=`
         let point='https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/Solonos%20Athens?zoomlevel=20&mapLayer=TrafficFlow&o=json&key='
         let place='Ymhttoy%72%20Athens'

         let test=`https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/${place}?mapLayer=TrafficFlow&o=json&key=`

         let mp=route+key
         sessionStorage.setItem("mp",route+key );


        let data = fetch(mp)



           .then(response=>{
               return response.json();
  }
           })
           .then(response=>{

           if (response.status==200){

        document.querySelector('#addresses').style.display = 'block';
        document.querySelector('#sub_route').style.display = 'block';
        document.querySelector('#map').style.display = 'block';
        document.querySelector('#map_pl').style.display = 'block';
        document.getElementById("map").src = mp;
        document.getElementById("id_departure").value = start.value;
        document.getElementById("id_destination").value = end.value;
        document.getElementById("id_destination").value = end.value;
        document.getElementById("id_map_pic").value=mp

        console.log(JSON.stringify(response));





         }
         else{

alert("address not found");

         }})
         .then(response => console.log("res: ", response))





         .catch(err => console.log("err: ", err));

         //console.log(data)


        }
        }

})


function subm_route(){
        let mp=sessionStorage.getItem('mp');
        let data = fetch(mp)

           .then(response=>{
       
       document.getElementById("map").src = mp;


        document.querySelector('#addresses').style.display = 'block';
        document.querySelector('#map').style.display = 'block';
        document.querySelector('#sub_route').style.display = 'block';


})


}
}

)
//document.querySelector('form').onsubmit=function()