from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostModelForm

# Create your views here.

def posts_list(request):
    all_posts = Post.objects.all()
    context = {
        'show_all_posts': all_posts
    }
    return render (request, "posts/posts_list.html", context)

#CRUD
#Create Retrieve Update and Delete

def posts_detail(request,slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': unique_post
    }
    return render (request, "posts/posts_detail.html", context)

def posts_create (request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        cellphone_num=799511474
    )
    form = PostModelForm (request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect ('/post/')
    context = {
        'showForm': form
    }
    return render (request, "posts/posts_create.html", context)
