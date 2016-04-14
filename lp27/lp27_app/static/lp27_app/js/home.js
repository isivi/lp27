$(function() {
  var scrollToFirstBlock = function() {
    $('html, body').animate({
      scrollTop: $(".block1").offset().top
    }, 1000);
  };

  $(".how-it-works").click(scrollToFirstBlock);
  $(".arrow-down").click(scrollToFirstBlock);
});