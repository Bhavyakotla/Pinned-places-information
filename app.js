function initAutocomplete() {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: -33.8688, lng: 151.2195 },
      zoom: 13,
      mapTypeId: "roadmap",
    })
};

// Create the search box and link it to the UI element.
const search = document.getElementById("search");
const searchBox = new google.maps.places.SearchBox(search);
map.controls[google.maps.ControlPosition.TOP_LEFT].push(search);

// Bias the SearchBox results towards current map's viewport.
map.addListener("bounds_changed", () => {
  searchBox.setBounds(map.getBounds());
});

let markers = [];
// Listen for the event fired when the user selects a prediction and retrieve more details for that place.
searchBox.addListener("places_changed", () => {
  const places = searchBox.getPlaces();
  if (places.length == 0) {
    return;
  }

  // For each place, get the icon, name and location.
  const bounds = new google.maps.LatLngBounds();
  places.forEach((place) => {
    if (!place.geometry || !place.geometry.location) {
      console.log("Returned place contains no geometry");
      return;
    }
    //const icon = {
      //url: place.icon,
      //size: new google.maps.Size(71, 71),
      //origin: new google.maps.Point(0, 0),
      //anchor: new google.maps.Point(17, 34),
      //scaledSize: new google.maps.Size(25, 25),
    //};
    
    // Create a marker for each place.
    markers.push(
      new google.maps.Marker({
        map,
        icon,
        title: place.name,
        position: place.geometry.location,
      })
    )
    })
    });

$('hover').hover(function(){
    $(this).css("background-color", "yellow");
});
  
$('#submit').on('click', function() {
    var info = $('#info').text();
    var data = {'latitude': 0.75, 'longitude': 1.15, 'info':info};

    $.ajax({
        type: "POST",
        url: "/pin_place/store",
        applicationType:'',
        data: JSON.stringify(data)
    }).done(function(response) {
         alert(response)
    });

});

