from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import random
import markdown2
class AddNewEntryForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content", help_text="write your content here")

    title.widget.attrs.update({'class': "titleclass"})
    content.widget.attrs.update({'class': "contentclass"})
def search_results(request):
    # if request.method=="GET":

    query=request.GET.get("q")
    print(query)
    entries=util.list_entries()
    s=str(query)
    for i in entries:
        if s==i:
            print ('ok')
            return entry(request,s)
        else:

            reslst = [i for i in entries if s in i]
            return render(request,"encyclopedia/search_results.html",{"reslst":reslst})
    else:
        return render(request,"encyclopedia/index.html")

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})

#create_new_page
def new(request):
    # check if method is POST
    if request.method=="POST":

        form=AddNewEntryForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            content=form.cleaned_data["content"]
            util.save_entry(title, content)
            return entry(request,title)

           
        else:
            #if the form is invalid
            return render(request,"encyclopedia/new.html",{"form":form})
        
    return render(request,'encyclopedia/new.html',{"form":AddNewEntryForm()})
#random_page
def random_entry(request):
    entries=util.list_entries()
    num=len(entries)
    print(num)
    num1=random.randint(0,num-1)
    print(num1)
    title=entries[num1]
    #shuffled=random.shuffle(entries)
    #title=shuffled[0]

    return entry(request,title)
def entry(request,title):
    text=util.get_entry(title)
    html=markdown2.Markdown().convert(text)

    return render(request, 'encyclopedia/entry.html', {"entry":html})

def edit_entry(request,title):
    if request.method=="GET":
        entry=util.get_entry(title)
        return render(request, "encyclopedia/edit_entry.html", {"content": entry,"title":title})

    if request.method=="POST":
        content=request.POST["content"]

        util.save_entry(content,title)

        return entry(request,title)

    return render(request, "encyclopedia/edit_entry.html")





