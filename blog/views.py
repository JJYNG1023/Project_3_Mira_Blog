from django.shortcuts import render, get_object_or_404
from .models import Post, Tag , Comment
from .forms import CommentForm

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

    # If the request method is not POST, create an empty instance of the CommentForm to be rendered in the template for users to submit new comments.
    # only authenticated users can submit comments, if the form is valid, it creates a new comment instance, associates it with the current post and the authenticated user, and saves it to the database. After saving the comment, it redirects the user back to the post detail page to see their newly added comment.
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
            
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
       
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/post_detail.html', context)
    