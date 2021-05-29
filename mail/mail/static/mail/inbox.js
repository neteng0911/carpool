document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#submit').addEventListener('click', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(inbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch('/emails/${mailbox}')
    .then(response => response.json())
    .then(emails => {

        if (emails.length==0) {

            const element = document.createElement('div');
            element.innerHTML="Nothing to see";
            console.log('empty list');



        }
        else {
            for (email in emails)
                {

                const sub=document.createElement('div');
                sub.innerHTML=email.subject;
                const recip=document.createElement('p');
                recip.innerHTML=email.recipients;



                }
        }

    }
    )}








    // Print emails
    //console.log(emails);

    // ... do something else with emails ...





function send_email() {
event.preventDefault();
const recipients= document.querySelector('#compose-recipients').value;
const subject= document.querySelector('#compose-subject').value;
const body= document.querySelector('#compose-body').value;

fetch('/emails', {
  method: 'POST',
  body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body,
  }),
  })
    // Take the return data and parse it in JSON format.
    .then((response) => response.json())
    .then((result) => {
      load_mailbox("sent", result);
    })
    .catch((error) => console.log(error));
};


function load_emails(mailbox,id) {




};