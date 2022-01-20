document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to like unlike

  document.querySelector('#like').addEventListener('click', like_post);
  document.querySelector('#unlike').addEventListener('click', unlike_post);

});

function like_post(post_id){

fetch(`/post/${post_id}`,{
  method: 'PUT',
  body: JSON.stringify({
      archived: true
        mypost_like_id = request.POST.get("post_to_like_id")
        mypost = Mypost.objects.get(id=mypost_like_id)
        mypost.likes.add(request.user)
        like_list=mypost.likes.all()
})

})

.then( () => load_mailbox("archive"));
}