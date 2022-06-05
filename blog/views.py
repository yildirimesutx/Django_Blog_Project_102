
from django.shortcuts import render, redirect
from .forms import NewPostForm, CommentForm
from .models import Comments, NewPost, Like
from django.contrib.auth.decorators import login_required

# Create your views here.

def about_page(request):
    return render(request, 'blog/about.html')


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

    context = {
       'post' : post,

    }

    return render(request, 'blog/post_list.html', context)

@login_required(login_url ='/auth/login')
def post_detail(request, id):
    blog = NewPost.objects.get(id=id)
    comment_form = CommentForm()
    comment_read = Comments.objects.filter(post=blog.id)
    blog.post_view += 1
    blog.save()
    number = len(comment_read)
    
    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           blog.comment_number += 1
           comment.post = blog
           comment.user = request.user
           blog.save()
           comment.save()

           return redirect("detail", id) 

          
     

    context = {
        "blog":blog,
        "comment_form":comment_form,
        "comment_read":comment_read,
        "number" :number
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

def post_like(request, id):
    blog = NewPost.objects.get(id=id)
    # like = Like.objects.get_or_create(user=request.user, blog=blog)
    # like.save()
    blog.post_like += 1
    blog.save()
    return redirect("detail", id)