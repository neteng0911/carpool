document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#edit_post').addEventListener('click', () => load_view('edit_post'));
  document.querySelector('#cancel').addEventListener('click', () => load_view('posts_view'));

  // By default, load the posts_view
  load_view('posts_view');
});

function load_view(view) {

  const posts_view = document.querySelector('#posts_view')
  document.querySelector('#edit_post').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  // Show the selected view and hide other views
 posts_view.style.display = 'block';
  document.querySelector('#edit_post').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';



function load_post(post_id){

alert('opening post '+ post_id);
  fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email => {
// show email and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-view').style.display = 'block';

    // creating the buttons inside the email

    const archive_button = document.createElement("button");
    const unarchive_button = document.createElement("button");
    const reply_button = document.createElement("button");
    const unread_button = document.createElement("button");


    var archive=email["archived"];
    var read=email["read"];
// naming the buttons
    archive_button.innerText="Archive";
    unarchive_button.innerText="Unarchive";
    unread_button.innerText="Mark Unread";
    reply_button.innerText='Reply';




    // display email (instead of writing in inbox.html)
    const view = document.querySelector('#email-view');
    view.innerHTML = `
      <ul>
        <li><b>From:</b> <span>${email['sender']}</span></li>
        <li><b>To: </b><span>${email['recipients']}</span></li>
        <li><b>Subject:</b> <span>${email['subject']}</span</li>
        <li><b>Time:</b> <span>${email['timestamp']}</span></li>
      </ul>
      <p>${email['body']}</p>
    `;

archive_button.className= "buttoncl";
archive_button.id= "archbtn";
unarchive_button.className= "buttoncl";
unread_button.className= "buttoncl";
//add buttons to the DOM

view.appendChild(reply_button);
reply_button.className= "buttoncl";
// toggle between archive and unarchive and unread buttons
if (archive){
view.appendChild(unarchive_button);
}
else {
view.appendChild(archive_button);

}

if (read){
view.appendChild(unread_button);

}
// add the eventlisteners to the buttons
archive_button.addEventListener('click', () => archive_email(email_id));
unarchive_button.addEventListener('click', () => unarchive_email(email_id));
unread_button.addEventListener('click', () => unread_email(email_id));
reply_button.addEventListener('click',  () => reply_email(email_id));



})

fetch(`/emails/${email_id}`,{
  method: 'PUT',
  body: JSON.stringify({
      read: true})
      })

};
