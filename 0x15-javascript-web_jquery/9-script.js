$(document).ready(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function(res) {
      // console.log(res);
      $('div#hello').text(res.hello);
    },
    error: function(xhr, status, error) {
      // Handle errors here
      console.error(xhr, status, error); 
    }
  });
});
