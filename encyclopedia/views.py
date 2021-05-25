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
def new(request):
    # check if method is POST
    if request.method=="POST":
        form=AddNewEntryForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            content=form.cleaned_data["content"]
            util.save_entry(title, content)
        
    return render(request,'encyclopedia/new.html',{"form":AddNewEntryForm()})
#random_page
def random(request):
    return render(request,'encyclopedia/random.html')
def entry(request,title):

    return render(request, 'encyclopedia/entry.html', {"entry":util.get_entry(title)})



