
from django.shortcuts import render, redirect
from .forms import NewPostForm, CommentForm
from .models import Comments, NewPost
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url ='/auth/login')
def newpost_add(request):
    form = NewPostForm() 
    

    if request.method == 'POST':
        form = NewPostForm(request.POST,  request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
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

@login_required(login_url ='/auth/login')
def post_detail(request, id):
    post = NewPost.objects.get(id=id)
    comment = CommentForm()
    comment_read = Comments.objects.all()
    
    if request.method =='POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save()
        
        return render(request, 'blog/post_detail.html',{"post":post,
        "comment":comment,
        "comment_read":comment_read} )  

    context = {
        "post":post,
        "comment":comment,
        "comment_read":comment_read
    }

    return render(request, 'blog/post_detail.html', context)

@login_required
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

@login_required
def post_delete(request, id):
    post = NewPost.objects.get(id=id)

    if request.method =='POST':
        post.delete()

        return redirect("list")

    context= {
        'post':post
    } 

    return render(request, 'blog/post_delete.html', context)   

  