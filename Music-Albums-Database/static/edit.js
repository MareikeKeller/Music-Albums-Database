function edit_album() {
  //updating ID
  let new_id = data_id.id;
  console.log("new id:");

  console.log(new_id);

  //dividing inputs into list items
  let genres_list = $("#genres_input").val();
  genres_list = genres_list.split(",");

  let awards_list = $("#awards_input").val();
  awards_list = awards_list.split(",");

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

  console.log(new_album);

  $.post(
    "/edit_route",
    JSON.stringify(new_album),
    function (result) {
      console.log(success);
    },
    "application/json"
  );
}

function display_entry() {
  let id_to_edit = data_id.id;

  $("#album_name_input").val(albums[id_to_edit]["album"]);
  $("#artist_name_input").val(albums[id_to_edit]["artist"]);
  $("#year_input").val(albums[id_to_edit]["year"]);
  $("#image_input").val(albums[id_to_edit]["cover"]);
  $("#summary_input").val(albums[id_to_edit]["summary"]);
  $("#records_input").val(albums[id_to_edit]["records_sold"]);
  $("#streams_input").val(albums[id_to_edit]["streams"]);
  $("#genres_input").val(albums[id_to_edit]["genres"]);
  $("#awards_input").val(albums[id_to_edit]["awards_won"]);
}

function show_new_entry() {
  let id_to_edit = data_id.id;
  $("#changed_result").empty();

  //creating link to new entry

  let url = "/results/" + id_to_edit;
  (window.location.href = url), true;
}

$(document).ready(function () {
  display_entry();

  //creating modal to confirm submission
  $(function () {
    $("#dialog").dialog({
      autoOpen: false,
      modal: true,
      show: "blind",
      hide: "blind",
      buttons: {
        "Confirm submission": function () {
          $("#edit_form").submit();
          $(this).dialog("close");
        },
        Cancel: function () {
          $(this).dialog("close");
        },
      },
    });

    $("#sumbit_album_btn").click(function () {
      $("#dialog").dialog("open");
      return false;
    });
  });

  $(function () {
    $("#dialog_discard").dialog({
      autoOpen: false,
      modal: true,
      show: "blind",
      hide: "blind",
      buttons: {
        "Discard submission": function () {
          show_new_entry();
          $(this).dialog("close");
        },
        Cancel: function () {
          $(this).dialog("close");
        },
      },
    });

    $("#discard_album_btn").click(function () {
      $("#dialog_discard").dialog("open");
      return false;
    });
  });

  // $("#discard_album_btn").click(function (e) {
  //   e.preventDefault();
  //   display_entry();
  // });

  $("#edit_form").submit(function (e) {
    e.preventDefault();
    edit_album();
    show_new_entry();
  });
});
