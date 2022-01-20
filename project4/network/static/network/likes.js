
   document.querySelectorAll('.fa-thumbs-up').forEach((like_button) => {
        like_button.onclick = () => {
            post_id = like_button.dataset.id;
            if(like_button.title == "LIKE")
            {
                document.querySelector(`#likes_${post_id}`).innerHTML++;
                like_button.title = "UNLIKE";
                like_button.style.color = "#fd8f00";
                like(post_id);
            }
            else
            {
                document.querySelector(`#likes_${post_id}`).innerHTML--;
                like_button.title = "LIKE";
                like_button.style.color = "";
                unlike(post_id);
            }
        }
    });
 function like(post_id)
{
    fetch(`/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
function unlike(post_id)
{
    fetch(`/unlike/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => console.log(data));
    }