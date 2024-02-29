$('document').ready(function () {
  $('input#btn_translate').click(translated);
  $('input#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translated();
      }
    });
  });
});

function translated () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(url + $.param({ lang: $('input#language_code').val() }), function (resp) {
    $('div#hello').html(resp.hello);
  });
}
