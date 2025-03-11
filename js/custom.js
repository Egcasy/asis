// Get Current Year
function getCurrentYear() {
    var d = new Date();
    var year = d.getFullYear();
    document.querySelector("#displayDateYear").innerText = year;
}
getCurrentYear()

//client section owl carousel
$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    navText: [
        '<i class="fa fa-long-arrow-left" aria-hidden="true"></i>',
        '<i class="fa fa-long-arrow-right" aria-hidden="true"></i>'
    ],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});

/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(8.947699, 7.454424),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

    // Add a marker at the specified location
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(8.947699, 7.454424),
        map: map,
        title: "My Location"
    });
}