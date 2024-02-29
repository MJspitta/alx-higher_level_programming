$(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(funciton () {
    let items = $('ul.my_list li');
    if (items.length > 0) {
      items[items.length - 1].remove();
    }
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
