from django.shortcuts import render, get_object_or_404
from .models import Post, Tag , Comment

# Create your views here.
def home(request):
    posts= Post.objects.filter(is_published=True)
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'blog/index.html', context)

# Get comment for a post and only display the main comment not the reply comment
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    comments = post.comments.filter(parent__isnull=True, is_approved=True)

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'blog/post_detail.html', context)
    