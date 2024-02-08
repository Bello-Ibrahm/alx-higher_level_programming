$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const lang_code = $('input#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang_code}`,
      method: 'GET',
      dataType: 'json',
      success: function (res) {
        // console.log(res); 
        $('div#hello').text(res.hello);
      },
      error: function (xhr, status, error) {
        // Handle errors here
        console.error(xhr, status, error);
      }
    });
  });
});
