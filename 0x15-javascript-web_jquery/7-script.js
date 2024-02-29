$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(resp, status) {
  if (status === 'success') {
    $('div#character').text(resp.name);
  }
});
