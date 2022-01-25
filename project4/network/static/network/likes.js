
   document.querySelectorAll('.likeunlike').forEach((element) => {
        element.onclick = () => {



            var post_id = element.dataset.id;


            console.log(post_id)
            if(element.title == "LIKE")
            {


                element.style.color = "#fd8f00";
                element.title="UNLIKE"
                element.innerHTML="Unlike"
                document.querySelector(`#likescounter_${post_id}`).innerHTML++;
                like(post_id);
            }
            else if (element.title == "UNLIKE")
            {   console.log(element)

                element.title="LIKE"
                element.innerHTML="Like"
                element.style.color = "";
                document.querySelector(`#likescounter_${post_id}`).innerHTML--;
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