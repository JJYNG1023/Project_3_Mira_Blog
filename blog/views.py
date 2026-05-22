from django.shortcuts import render
from .models import Post, Tag

# Create your views here.
def home(request):
    posts= Post.objects.filter(is_published=True)
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'blog/index.html', context)
    
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

    