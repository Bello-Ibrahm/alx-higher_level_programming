$(document).ready(() => {
  // On button click
  $('input#btn_translate').click(() => {
    const lang_code = $('input#language_code').val();
    fetchLangTranslation(lang_code);
  });

  // On enter keypress 
  $('input#language_code').keypress(function (evt) {
    if (evt.which === 13){
        const lang_code = $(this).val();
        fetchLangTranslation(lang_code);
    }
  });

  const fetchLangTranslation = (lang_code) => {
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang_code}`,
      method: 'GET',
      dataType: 'json',
      success: function (res) {
        $('div#hello').text(res.hello);
      },
      error: function (xhr, status, error) {
        console.error(xhr, status, error);
      }
    });
  }
});
