function add_album() {
  //updating ID
  let new_id = Object.keys(albums).length + 1;

  //dividing inputs into list items
  let genres_list = $("#genres_input").val();
  genres_list = genres_list.split(", ");

  let awards_list = $("#awards_input").val();
  awards_list = awards_list.split(", ");

  //creating new entry
  albums[new_id] = {};

  albums[new_id]["id"] = new_id;
  albums[new_id]["album"] = $("#album_name_input").val();
  albums[new_id]["artist"] = $("#artist_name_input").val();
  albums[new_id]["cover"] = $("#image_input").val();
  albums[new_id]["year"] = $("#year_input").val();
  albums[new_id]["summary"] = $("#summary_input").val();
  albums[new_id]["records_sold"] = $("#records_input").val();
  albums[new_id]["streams"] = $("#streams_input").val();
  albums[new_id]["awards_won"] = awards_list;
  albums[new_id]["genres"] = genres_list;

  new_album = albums[new_id];

  $.ajax({
    type: "POST",
    url: "add_route",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(new_album), //into server
    success: function (result) {
      albums = result["albums"]; //this is getting data from server

      //this works
      console.log("DEBUG");
      console.log(albums);
      console.log("DEBUG");

      //empty fields
      $("#album_name_input").val("");
      $("#artist_name_input").val("");
      $("#image_input").val("");
      $("#year_input").val("");
      $("#summary_input").val("");
      $("#records_input").val("");
      $("#streams_input").val("");
      $("#awards_input").val("");
      $("#genres_input").val("");

      $("#album_name_input").focus();
    }, //end of success

    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}

function show_new_entry() {
  $("#new_result").empty();

  //creating link to new entry
  let id_to_add = Object.keys(albums).length;
  let url = "/results/" + id_to_add;
  let new_link = $(
    "<div class='top' id='item_created_alert'><b> New item successfully created!</b><div> <div id='preview_link'> <a href='" +
      url +
      "' class='link-primary'>" +
      "Click here to look at your new entry" +
      "</a> </div>"
  );

  $("#new_result").append(new_link);
}

$(document).ready(function () {
  console.log(albums);
  $("#add_form").submit(function (e) {
    e.preventDefault();
    add_album();
    show_new_entry(); //important that this is called second so that the ID's don't get mixed up
  });
});
