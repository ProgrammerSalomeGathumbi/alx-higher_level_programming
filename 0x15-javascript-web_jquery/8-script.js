$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      const movie = data.results;
      for (let m = 0; m < movie.length; m++) {
        $('#list_movies').append(`<li>${movie[m].title}</li>`);
      }
    }
  });
});
