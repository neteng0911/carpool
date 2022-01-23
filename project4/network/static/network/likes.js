
   document.querySelectorAll('.likeunlike').forEach((like_button) => {
        button.onclick = () => {
            post_id = this.dataset.id;
            if(like_button.title == "like_button")
            {
                document.querySelector(`#likes1`).innerHTML++;

                like_button.style.color = "#fd8f00";
                like(post_id);
            }
            else
            {
                document.querySelector(`#likes1`).innerHTML--;

                like_button.style.color = "";
                unlike(post_id);
            }
        }
    });
 function like(post_id)
{
    fetch(`post/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
function unlike(post_id)
{
    fetch(`post/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
    }