var scrollToFlow = function() {
    $('html, body').animate({
        scrollTop: ($('.flow1').offset().top)
    }, 1200);
};

$(function() {
    $('.how-it-works').click(scrollToFlow);
});
