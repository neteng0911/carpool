from django.shortcuts import render
from django import forms
from . import util
class AddNewEntryForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
#create_new_page
def new(request,title,content):
    return render(request,'encyclopedia/new.html', {"title":util.save_entry(title,content),"form":AddNewEntryForm()})
#random_page
def random(request):
    return render(request,'encyclopedia/random.html')
def entry(request,title):

    return render(request, 'encyclopedia/entry.html', {"title":util.get_entry(title)})




