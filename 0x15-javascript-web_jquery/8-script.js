$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (resp, status) {
  if (status === 'success') {
    let film = resp.results;
    for (let i in film) {
      $('ul#list_movies').append('<li>' + film[i].title + '</li>');
    }
  }
});
