
   document.querySelectorAll('.likeunlike').forEach((button) => {
        button.onclick = () => {



            var post_id = button.dataset.id;


            console.log(post_id)
            if(button.title == "LIKE")
            {
                document.querySelector(`#${post_id}_likescounter`).innerHTML++;

                button.style.color = "#fd8f00";
                button.style.title="UNLIKE"
                button.value="Unlike"
                like(post_id);
            }
            else if (button.title == "UNLIKE")
            {   console.log(button)
                document.querySelector(`#${post_id}_likescounter`).innerHTML--;
                button.style.title="LIKE"
                button.value="Like"
                button.style.color = "";
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