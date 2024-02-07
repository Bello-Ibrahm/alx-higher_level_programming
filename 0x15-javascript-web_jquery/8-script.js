$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    // dataType: 'json',
    success: function(res) {
      // console.log(res);
      for (i = 0; i < res.results.length; i++){
         $('ul#list_movies').append(`<li>${res.results[i].title}</li>`);
      } 
    },
    error: function(xhr, status, error) {
      // Handle errors here
      console.error(xhr, status, error); 
    }
  });
});
