window.setInterval(function() {
    var array = [];
    var links = document.links;
    for(var i = 0; i < links.length; i++) 
    {
        if (links[i].href.includes("maps/place")) {
            console.log(links[i].href);
        }
    }
}, 500);