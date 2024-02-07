$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    // dataType: 'json',
    success: function(res) {
      // console.log(response); 
      $('div#character').text(res.name);
    },
    error: function(xhr, status, error) {
      // Handle errors here
      console.error(xhr, status, error); 
    }
  });
});
