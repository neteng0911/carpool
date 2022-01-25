
   document.querySelectorAll('.likes').forEach((button) => {
        button.onclick = () => {
            post_id = this.dataset.id;
            if(like_button.title == "LIKE")
            {
                document.querySelector(`#likes_{{post.id}}`).innerHTML++;

                like_button.style.color = "#fd8f00";
                like(post_id);
            }
            else
            {
                document.querySelector(`#likes_{{post.id}}`).innerHTML--;

                like_button.style.color = "";
                unlike(post_id);
            }
        }
    });
 function like(post_id)
{
    fetch(`like/post/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
function unlike(post_id)
{
    fetch(`unlike/post/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
    }