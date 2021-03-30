#git completed
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

    query=request.GET.get("q")
    #print(query)
    entries=util.list_entries()
    s=str(query)

    for i in entries:
        if s.upper()==i or s.lower()==i:
            return entry(request,s)
        else:


            reslst = [i for i in entries if s.upper() in i or s.lower() in i or s in i]
            if reslst==[]:
                return render(request,"encyclopedia/no_results.html")
            else:
                return render(request,"encyclopedia/search_results.html",{"reslst":reslst})

    return render(request,"encyclopedia/search_results.html",{"reslst":reslst})

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
    choice=random.choice(util.list_entries())

    return entry(request,choice)


def entry(request,title):
    text = util.get_entry(title)
    print(text)
    if text is None:
        return render(request, "encyclopedia/entry.html", {"Edit": 'Create',"entry": 'ERROR_entry not found', "title": title})


    else:
        html=markdown2.Markdown().convert(text)
    return render(request, 'encyclopedia/entry.html', {"entry": html, "title": title})


def edit_entry(request,title):
    if request.method=="GET":
        text=util.get_entry(title)
        return render(request, "encyclopedia/edit_entry.html", {"Edit": 'Edit',"content": text,"title":title})

    if request.method=="POST":
        new_content=request.POST["content"]


        util.save_entry(title,new_content)

        return entry(request,title)

    return render(request, "encyclopedia/edit_entry.html")





