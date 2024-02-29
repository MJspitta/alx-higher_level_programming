$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('input#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('input#language_code').val() }), function (resp) {
      $('div#hello').html(resp.hello);
    });
  });
});
