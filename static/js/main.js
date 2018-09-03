$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    var navtop = $('nav').offset().top;
    console.log(navtop);
    $(window).scroll(function() {
        if ($(window).scrollTop() > navtop) {
            $('nav').addClass('nfixed');
            // $('nav').css('background-color', 'rgba(32, 79, 128, 1)');
        }
        else {
            $('nav').removeClass('nfixed');
            var alpha = $(window).scrollTop() / navtop;
            // $('nav').css('background-color', 'rgba(32, 79, 128, '+ alpha + ')');
        }
    });
});