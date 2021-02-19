from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
#create_new_page
def new(request,title,content):
    return render(request,'encyclopedia/new.html', {"title":util.save_entry(title,content)})
#random_page
def random(request):
    return render(request,'encyclopedia/random.html')
def entry(request,title):

    return render(request, 'encyclopedia/entry.html', {"title":util.get_entry(title)})




