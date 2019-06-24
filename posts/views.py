from django.shortcuts import render, get_object_or_404
from .models import Post

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