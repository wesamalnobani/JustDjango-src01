from django.shortcuts import render
from .models import Post

# Create your views here.

def posts_list(request):
    show = Post.objects.all()
    context = {
        'all_posts': show
    }
    return render (request, "posts/posts_list.html", context)
