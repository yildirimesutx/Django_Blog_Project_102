import re
from django.shortcuts import render, redirect
from .forms import NewPostForm

# Create your views here.

def newpost_add(request):
    form = NewPostForm() 
    print(request.POST)

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("home")



    context = {
       "form":form
    }

    return render(request, "blog/newpost_add.html", context)
