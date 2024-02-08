$(document).ready(() => {
  // Add item onclick
  $('div#add_item').click(() => {
    $('ul.my_list').append(`<li>Item</li>`);
  });
  // Remove item onclick
  $('div#remove_item').click(() => {
    $('ul.my_list li:last-child').remove();
  });
  // clear all item onclick
  $('div#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
