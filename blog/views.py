
from django.shortcuts import render, redirect
from .forms import NewPostForm
from .models import NewPost

# Create your views here.

def newpost_add(request):
    form = NewPostForm() 
    print(request.POST)

    if request.method == 'POST':
        form = NewPostForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect("list")

    context = {
       "form":form
    }

    return render(request, "blog/newpost_add.html", context)



def post_list(request):

    post = NewPost.objects.all()
    print(post)
    context = {
       'post' : post
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post = NewPost.objects.get(id=id)

    context = {
        "post":post
    }

    return render(request, 'blog/post_detail.html', context)


def post_update(request, id):
    post = NewPost.objects.get(id=id)
    form = NewPostForm(instance=post)

    if request.method == 'POST':
       form = NewPostForm(request.POST,  request.FILES or None, instance=post)
       if form.is_valid():
           form.save()

           return redirect("list")

    context = {
        "form" : form
    }       

    return render(request, "blog/post_update.html", context)       


def post_delete(request, id):
    post = NewPost.objects.get(id=id)

    if request.method =='POST':
        post.delete()

        return redirect("list")

    context= {
        'post':post
    } 

    return render(request, 'blog/post_delete.html', context)   

  