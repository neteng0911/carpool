from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
#create_new_page
def new(request):
    return render(request,'encyclopedia/new.html')
#random_page
def random(request):
    return render(request,'encyclopedia/random.html')
def entry(request,title):
    #context ={"title" : title}
    return render(request, "encyclopedia/entry.html", {"title":util.convert_md(title)})
    

