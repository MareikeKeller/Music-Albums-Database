function load_results(found_matches) {
  $("#search_results_div").empty();

  if (found_matches.length == 0) {
    let no_results_message = $(
      "<div id='results_message'> No results found for <b>" +
        JSON.stringify(search_term) +
        "</b>! </div>"
    );

    $("#search_results_div").append(no_results_message);
  } else {
    // console.log(artist);
    let results_message = $(
      "<div id='results_message'> We found <b>" +
        found_matches.length +
        " </b> albums matching your search term <b>" +
        JSON.stringify(search_term) +
        "</b></div>"
    );

    $("#search_results_div").append(results_message);

    //sorting search results for page
    found_matches.sort((a, b) => (a.artist > b.artist ? 1 : -1));

    for (index in found_matches) {
      let artist = found_matches[index].artist;
      let album = found_matches[index].album;
      let id = found_matches[index].id;

      // console.log(id);
      let url = "/results/" + id;
      let new_link = $(
        "<div id='results'> <a href='" +
          url +
          "' class='link-primary'>" +
          artist +
          "  -  " +
          album +
          "</a> </div>"
      );

      $("#search_results_div").append(new_link);
    }
  }
}

$(document).ready(function () {
  load_results(found_matches);
});
