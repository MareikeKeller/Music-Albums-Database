function display_toplist() {
  $("#popular_search").empty();
  for (index in albums) {
    let artist = albums[index].artist;
    let album = albums[index].album;
    let id = albums[index].id;
    let cover = albums[index].cover;
    let summary = albums[index].summary;

    // let preview_text = summary.split(".", 1)[0];
    let preview_text = summary.slice(0, 131);

    console.log(id);
    let url = "/results/" + id;

    let new_link =
      "<div id='card_div' class'col-4-md'><div class='card' style='width: 16rem;''><a href='" +
      url +
      "'><img class='card-img-top' src='" +
      cover +
      "' alt='Card image as album cover of " +
      artist +
      "'></a><div class='card-body'><h5 class='card-title'>" +
      album +
      "</h5><h6 class='card-subtitle mb-2 text-muted'>" +
      artist +
      "</h6><p class='card-text subtext'>" +
      preview_text +
      "...</p><a href='" +
      url +
      "' class='btn btn-primary stretched-link'>See Album</a></div></div></div>";

    //console.log(new_link);

    $("#popular_search").append(new_link);

    if (index > 2) {
      break;
    }
  }
}

$(document).ready(function () {
  display_toplist();
});
