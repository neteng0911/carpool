
    var BingMapsKey = 'Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF';
      
    function geocode() {
        var start = document.getElementById('dep').value;
        var end= document.getElementById('dest').value;

        var geocodeRequeststart = "http://dev.virtualearth.net/REST/v1/Locations?query=" + encodeURIComponent(start) + "&jsonp=GeocodeCallback&key=" + BingMapsKey;
        var geocodeRequestend = "http://dev.virtualearth.net/REST/v1/Locations?query=" + encodeURIComponent(end) + "&jsonp=GeocodeCallback&key=" + BingMapsKey;
        CallRestService(geocodeRequeststart, GeocodeCallback);
        CallRestService(geocodeRequestend, GeocodeCallback);
    }

    function GeocodeCallback(response) {
        var output = document.getElementById('output');

        if (response &&
            response.resourceSets &&
            response.resourceSets.length > 0 &&
            response.resourceSets[0].resources) {

            var results = response.resourceSets[0].resources;
            console.log(results[0].point.coordinates[0],results[0].point.coordinates[1])

            var html = ['<table><tr><td>Name</td><td>Latitude</td><td>Longitude</td></tr>'];

            for (var i = 0; i < results.length; i++) {
                html.push('<tr><td>', results[i].name, '</td><td>', results[i].point.coordinates[0], '</td><td>', results[i].point.coordinates[1], '</td></tr>');
            }

            html.push('</table>');

            output.innerHTML = html.join('');
        } else {
            output.innerHTML = "No results found.";
        }
    }

    function CallRestService(request) {
        var script = document.createElement("script");
        script.setAttribute("type", "text/javascript");
        script.setAttribute("src", request);
        document.body.appendChild(script);
    }
