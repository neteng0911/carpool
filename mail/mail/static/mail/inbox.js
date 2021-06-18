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


        if (result.error) {
            console.log(result.error);
            alert(result.error)

        }




      load_mailbox("sent", result);
    })


};

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';


}


function load_mailbox(mailbox) {

  const email_view = document.querySelector('#emails-view')
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  // Show the mailbox and hide other views
  email_view.style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  email_view.innerHTML = '';
  email_view.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
// create headers for the rows

        const h_mail = document.createElement("div");
        h_mail.style.backgroundColor = 'gray';
        email_view.appendChild(h_mail);
        h_mail.style.borderStyle = 'solid';
        h_mail.style.borderColor = 'black';
        h_mail.style.borderWidth = '0.1rem';
        h_mail.style.marginBottom = '0.2rem';

        const h_sender = document.createElement('h5');
        h_sender.innerHTML='sender'
        h_sender.style.display = 'inline-block';
        h_sender.style.marginLeft = '5rem';


        const h_rec=document.createElement('h5');
        h_rec.innerHTML='recipients'
        h_rec.style.display = 'inline-block';
        h_rec.style.marginLeft = '10rem';

        const h_sub = document.createElement('h5');
        h_sub.innerHTML='subject'
        h_sub.style.display = 'inline-block';
        h_sub.style.marginLeft = '10rem';

        const h_time = document.createElement('h5');
        h_time.innerHTML='date'
        h_time.style.display = 'inline-block';
        h_time.style.margin = '0.5rem';
        h_time.style.float="right";

        h_mail.appendChild(h_sender);
        h_mail.appendChild(h_sub);
        h_mail.appendChild(h_rec);

        h_mail.appendChild(h_time);

          //const trt=document.getElementById('emails-view');
          //const trt=document.getElementsByTagName('p')

  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {

      if (emails.length == 0) {
        email_view.innerHTML = '<p style = "font-size: large; font-weight: bold;">Empty!</p>';
      }
      else {
        for (email in emails) {

          const mail = document.createElement("div");
          const sender = document.createElement('h5');
          const rec=document.createElement('p');
          const sub = document.createElement('p');
          const time = document.createElement('p');
          //const id = document.createElement('p');

          
/*          //what happens when a user clicks on an email in the mailbox

          const parent_element = document.createElement("div");
          mail.addEventListener('click', () => load_email(emails[email].id));
          parent_element.addEventListener('click', () => load_email(emails[email].id));
          sub.addEventListener('click', () => load_email(emails[email].id));
          time.addEventListener('click', () => load_email());
          sender.addEventListener('click', () => load_email());*/

          rec.innerHTML=emails[email].recipients;

          sender.innerHTML = emails[email].sender;
          if (emails[email].subject == '') {
            sub.innerHTML = 'No Subject';
            sub.style.color = 'red';
          }
          else {
            sub.innerHTML = emails[email].subject;
          }
          time.innerHTML = emails[email].timestamp;

          mail.style.borderStyle = 'solid';
          mail.style.borderColor = 'black';
          mail.style.borderWidth = '0.1rem';
          mail.style.marginBottom = '0.2rem';
          if (emails[email].read == true) {
            mail.style.backgroundColor = 'lightgray';
          }
          else {
            mail.style.backgroundColor = 'white';
          }
          mail.classList.add('container');
          mail.classList.add('mail');

          sender.style.display = 'inline-block';
          sender.style.marginLeft = '0.5rem';
          sender.id="send"


          rec.style.display = 'inline-block';
          rec.style.paddingLeft = '5rem';
          rec.style.color='green';

          sub.style.display = 'inline-block';
          sub.style.marginLeft= '5rem';


          time.style.display = 'inline-block';
          time.style.marginLeft = '0.5rem';
          time.style.float = 'right';
          time.style.color = 'blue';

          email_view.appendChild(mail);
          mail.appendChild(sender);
          mail.appendChild(sub);
          mail.appendChild(time);
          //mail.appendChild(id);
          mail.appendChild(rec);

          mail.addEventListener('mouseenter',over,false);
          mail.addEventListener('mouseleave',out,false);

         function over (event){

                event.target.style.color="blue";
                event.target.style.cursor='pointer';

          }

         function out (event){

                event.target.style.color="black";
                event.target.style.cursor='default';

          }




        }




      }
    }

    );





}

function load_email(email_id){

  fetch(`/emails/<int:email_id>`)

    .then(response => response.json())
    .then(email => {

        const h_mail = document.createElement("div");
        h_mail.style.backgroundColor = 'gray';
        email_view.appendChild(h_mail);
        h_mail.style.borderStyle = 'solid';
        h_mail.style.borderColor = 'black';
        h_mail.style.borderWidth = '0.1rem';
        h_mail.style.marginBottom = '0.2rem';

          const mail = document.createElement("div");
          const sender = document.createElement('h5');
          const rec=document.createElement('p');
          const sub = document.createElement('p');
          const time = document.createElement('p');

          sender.innerHTML='email.sender';
          rec.innerHTML='${email["rec"]}';



    sub.innerHTML = '<p style = "font-size: large; font-weight: bold;">${email.subject}</p>';



    })

};



