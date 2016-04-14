var scrollToFlow = function() {
    $('html, body').animate({
        scrollTop: ($('.feature-start').offset().top)
    }, 1200);
};

$(function() {
    $('.how-it-works').click(scrollToFlow);
});
