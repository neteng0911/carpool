
   document.querySelectorAll('.likes').forEach((button) => {
        button.onclick = () => {
        console.log(button)
            var post_id = button.dataset.id;
            if(button.title == "LIKE")
            {
                document.querySelector(`#like_counter`).innerHTML++;

                button.style.color = "#fd8f00";
                like(post_id);
            }
            else if (button.title == "UNLIKE")
            {   console.log(button)
                document.querySelector(`#likes_counter`).innerHTML--;
                alert("Hello! I am an alert box!!");
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