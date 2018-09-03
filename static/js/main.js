$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    var nav_offset = $('nav').offset();
    console.log($('nav').height());
    console.log(nav_offset.top);
    $("#space-holder").height($('nav').height());
    //$(window).scroll(function() {
    //    if ($(window).scrollTop() > navtop) {
    //        $('nav').addClass('nfixed');
    //        // $('nav').css('background-color', 'rgba(32, 79, 128, 1)');
    //    }
    //    else {
    //        $('nav').removeClass('nfixed');
    //        var alpha = $(window).scrollTop() / navtop;
    //        // $('nav').css('background-color', 'rgba(32, 79, 128, '+ alpha + ')');
    //    }
    //});
});
