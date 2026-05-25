from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse
from django.contrib import messages
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

    edit_comment_id = request.GET.get('edit_comment')
    edit_comment = None
    edit_comment_form = None

    if edit_comment_id and request.user.is_authenticated:
        edit_comment = get_object_or_404(Comment, id=edit_comment_id, post=post, author=request.user)

    edit_comment_form = CommentForm(instance=edit_comment)

    # If the request method is not POST, create an empty instance of the CommentForm to be rendered in the template for users to submit new comments.
    # only authenticated users can submit comments, if the form is valid, it creates a new comment instance, associates it with the current post and the authenticated user, and saves it to the database. After saving the comment, it redirects the user back to the post detail page to see their newly added comment.
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
        
        comment_id = request.POST.get('comment_id')

    #update/edit exiting comment       
        if comment_id : 
            comment = get_object_or_404(Comment, id=comment_id, post=post, author=request.user)
        
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Comment has been updated')
            return redirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}#comment-{comment.id}")

    #create new comment
        else:
            comment_form = CommentForm(data=request.POST)
    
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment has been posted')

            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
       
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'edit_comment': edit_comment,
        'edit_comment_form': edit_comment_form,
    }

    return render(request, 'blog/post_detail.html', context)
    