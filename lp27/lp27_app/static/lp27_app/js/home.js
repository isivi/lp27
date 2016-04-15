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

  var submitMainForm = function(event) {
    event.preventDefault();
    var value = $('#second-submit-button').parent().find('input[type="text"]').val();
    $submit_form = $('#first-submit-button').parent();
    $submit_form.find('input[type="text"]').val(value);
    $submit_form.submit();
  };

  $(".how-it-works").click(scrollToFirstBlock);
  $(".go-to-form").click(scrollToFormBlock);
  $(".arrow-down").click(scrollToFirstBlock);
  $("#second-submit-button").click(submitMainForm);
});
