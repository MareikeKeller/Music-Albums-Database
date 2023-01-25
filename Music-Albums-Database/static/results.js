$(document).ready(function () {
  //getting id from URL for edit button
  $("#edit_album_btn").click(function () {
    let url = window.location.href;
    let id_to_edit = url.substring(url.lastIndexOf("/") + 1);

    (window.location.href = "/edit/" + id_to_edit), true;
  });
});
