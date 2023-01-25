//Inputs search term into url
function redirect() {
  let new_search_input = $("#form_input").val();
  (window.location.href = "/search/" + new_search_input), true;

  if (new_search_input.length == 0) {
    alert("Search input needed");
    (window.location.href = "/"), true;
  }
}

$(document).ready(function () {
  $(".add_button").click(function () {
    (window.location.href = "/add"), true;
  });

  $("#search_form").submit(function (e) {
    e.preventDefault();
    redirect();
    $("#search_form").focus();
  });

  $("#submit_button").click(function () {
    $("#submit_button").submit();
  });
});
