
   document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('form').onsubmit=function() {
        element.onclick = () => {

alert("Hello! I am an alert box!!");
         let start='Ymhttou%2072%20Athens'
         let end='Skoufa%202%20Athens'
         'https://dev.virtualearth.net/REST/v1/Imagery/Map/imagerySet/centerPoint/zoomLevel/Routes/\
         travelMode?waypoint.1={routeWaypoint1}&waypoint.2={routeWaypoint2}\
         &waypoint.n={routeWaypointn}&mapSize={mapSize}\
         &avoid={avoidOptions}&pushpin={pushpin}&timeType={timetType}&dateTime={dateTime}\
         &maxSolutions={maxSolutions}\
         &distanceBeforeFirstTurn={distanceBeforeFirstTurn}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&&o=json&key='
         let key='Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF'
         let route=`https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=${start}1&wp.1=${end}2&o=json&key=`
         let point='https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/Solonos%20Athens?zoomlevel=20&mapLayer=TrafficFlow&o=json&key='
         let place='Ymhttoy%72%20Athens'

         let test=`https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/${place}?mapLayer=TrafficFlow&o=json&key=`
         let mp=route+key
        let data = fetch(mp)
         .then(response => console.log("res: ", response))
         .catch(err => console.log("err: ", err));
         console.log(data)
        document.getElementById("map").src = mp;
        }}})
