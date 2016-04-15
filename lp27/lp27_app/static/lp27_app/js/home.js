$(function() {
  var scrollToFirstBlock = function() {
    $('html, body').animate({
      scrollTop: $(".block1").offset().top
    }, 1000);
  };

  var scrollToFormBlock = function() {
    $('html, body').animate({
      scrollTop: $(".block4").offset().top
    }, 1000);
  };

  $(".how-it-works").click(scrollToFirstBlock);
  $(".go-to-form").click(scrollToFormBlock);
  $(".arrow-down").click(scrollToFirstBlock);
});
