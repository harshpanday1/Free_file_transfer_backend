// Script to auto hide the alert after 3s

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slidUP(500, function(){
        $(this).remove();
    });
},3000);