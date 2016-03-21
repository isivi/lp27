var scrollToForm = function() {
    $('html, body').animate({
        scrollTop: ($('.typeform').offset().top)
    }, 1500);
};

$(function() {
    $('.how-it-works').click(scrollToForm);
});
