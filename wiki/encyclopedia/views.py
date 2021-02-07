from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create_new_page(request):
    return render(request,'encyclopedia/new.html')

def random_page(request):
    return render(request,'encyclopedia/random.html')

