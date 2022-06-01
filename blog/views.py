import re
from django.shortcuts import render, redirect
from .forms import NewPostForm
from .models import NewPost

# Create your views here.

def newpost_add(request):
    form = NewPostForm() 
    print(request.POST)

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("list")

    context = {
       "form":form
    }

    return render(request, "blog/newpost_add.html", context)



def post_list(request):

    post = NewPost.objects.all()

    context = {
       'post' : post
    }

    return render(request, 'blog/post_list.html', context)

