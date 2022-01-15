document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#edit').addEventListener('click', () => load_view('edit'));
  document.querySelector('#cancel').addEventListener('click', () => load_view('index'));


});