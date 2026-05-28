from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse
from django.contrib import messages
from .models import Post, Tag , Comment, PostImage
from .forms import CommentForm , PostForm

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
    
    #reply comment
    reply_to_id = request.GET.get('reply_to')  
    reply_to_comment = None

    if reply_to_id and request.user.is_authenticated:
        reply_to_comment = get_object_or_404(Comment, id=reply_to_id, post=post, parent__isnull=True, is_approved=True)

    # If the request method is not POST, create an empty instance of the CommentForm to be rendered in the template for users to submit new comments.
    # only authenticated users can submit comments, if the form is valid, it creates a new comment instance, associates it with the current post and the authenticated user, and saves it to the database. After saving the comment, it redirects the user back to the post detail page to see their newly added comment.
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
        
        comment_id = request.POST.get('comment_id')
        delete_comment_id = request.POST.get('delete_comment_id')
        parent_id = request.POST.get('parent_id')


    #delete exiting comment       
        if delete_comment_id:
            comment = get_object_or_404(Comment, id=delete_comment_id, post=post, author=request.user)
            comment.delete()
            messages.success(request, 'Comment has been deleted')
            return redirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}#comments")

    #update/edit exiting comment       
        elif comment_id : 
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

                parent_id = request.POST.get('parent_id')
                if parent_id:
                    parent_comment = get_object_or_404(Comment, id=parent_id, post=post, parent__isnull=True)
                    comment.parent = parent_comment

                comment.save()

                if parent_id:
                    messages.success(request, 'Reply has been posted')
                    return redirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}#comment-{parent_id}")

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
        'reply_to_comment': reply_to_comment,
    }

    return render(request, 'blog/post_detail.html', context)

#like and unlike post
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    if not request.user.is_authenticated:
        return redirect('account_login')

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.success(request, 'Post removed from liked posts.')
    else:
        post.likes.add(request.user)
        messages.success(request, 'Post added to liked posts.')

    return redirect(
        f"{reverse('post_detail', kwargs={'slug': post.slug})}#post-actions")


# like and unlike comment
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, is_approved=True)
    post = comment.post

    if not request.user.is_authenticated:
        return redirect('account_login')

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
        messages.success(request, 'Comment like removed.')
    else:
        comment.likes.add(request.user)
        messages.success(request, 'Comment liked.')

    return redirect(
        f"{reverse('post_detail', kwargs={'slug': post.slug})}#comment-{comment.id}")


# Add bookmark and remove bookmark for post
def bookmark_post(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    if not request.user.is_authenticated:
        return redirect('account_login')

    if request.user in post.bookmarked.all():
        post.bookmarked.remove(request.user)
        messages.success(request, 'Post removed from bookmarks.')
    else:
        post.bookmarked.add(request.user)
        messages.success(request, 'Post bookmarked.')

    return redirect(
        f"{reverse('post_detail', kwargs={'slug': post.slug})}#post-actions"
    )


# Show all bookmarked posts
def bookmarked_posts(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    posts = Post.objects.filter(
        bookmarked=request.user,
        is_published=True)

    tags = Tag.objects.filter(
        posts__bookmarked=request.user, posts__is_published=True).distinct()

    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'blog/bookmark.html', context)


# Show posts created by the logged-in user
def my_blog(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    posts = Post.objects.filter(
        author=request.user,
        is_published=True
    )

    tags = Tag.objects.filter(
        posts__author=request.user,
        posts__is_published=True
    ).distinct()

    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'blog/my_blog.html', context)

# create post view and form 
def create_post(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        images = request.FILES.getlist('images')
        tag_names = request.POST.get('tag_names', '')

        if len(images) > 5:
            messages.error(request, 'You can upload a maximum of 5 images.')

        elif post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.is_published = True
            post.save()

            #create tags
            tags = [
                tag.strip().replace('#','')
                for tag in tag_names.split(',')
                if tag.strip()
            ]

            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

            #save uploaded images
            first_post_image = None

            for image in images:
                post_image = PostImage.objects.create(
                    post=post,
                    image=image
                )
                if first_post_image is None:
                    first_post_image = post_image

            #use first image as the featured image for the blog post
            if first_post_image:
                post.featured_image = first_post_image.image
                post.save(update_fields=['featured_image'])
            messages.success(request, 'Post has been created.')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'Please check the form and try again.')
    else:
        post_form = PostForm()

    context = {
        'post_form': post_form,
    }

    return render(request, 'blog/create_post.html', context)

#edit post content and update post form
def edit_post(request, slug):
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    post = get_object_or_404(Post, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        tag_names = request.POST.get('tag_names', '')
        images = request.FILES.getlist('images')

        if len(images)>5:
            messages.error(request,'You can only upload 5 images')

        elif post_form.is_valid():
            post= post_form.save(commit=False)
            post.author = request.user
            post.is_published = True
            post.save()
           
            #update tags
            post.tags.clear()
            tags = [
                tag.strip().replace('#', '')
                for tag in tag_names.split(',')
                if tag.strip()
            ]
            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
            
            # add new uploaded images
            first_new_image = None
            for image in images:
                post_image = PostImage.objects.create(
                    post=post,
                    image=image
                )

                if first_new_image is None:
                    first_new_image = post_image

            # if no featured image exists, use the first new image
            if first_new_image:
                post.featured_image = first_new_image.image
                post.save(update_fields=['featured_image'])

            messages.success(request, 'Post has been updated.')
            return redirect('post_detail', slug=post.slug)
        else: messages.error(request,'please check the form and try again')
    else:
        post_form = PostForm(instance=post)

    existing_tags = ','.join([tag.name for tag in post.tags.all()])

    context = {
        'post': post,
        'post_form': post_form,
        'existing_tags': existing_tags,
        'existing_images': post.images.all(),
    }
    return render(request, 'blog/edit_post.html', context)

# delete image from existing post
def delete_post_image(request, image_id):
    if not request.user.is_authenticated:
        return redirect('account_login')

    image = get_object_or_404(
        PostImage,
        id=image_id,
        post__author=request.user
    )

    post = image.post

    # Find another image to use as featured image if needed
    next_image = post.images.exclude(id=image.id).first()

    if post.featured_image and post.featured_image.name == image.image.name:
        if next_image:
            post.featured_image = next_image.image
        else:
            post.featured_image = None

        post.save(update_fields=['featured_image'])

    image.delete()

    messages.success(request, 'Image has been deleted.')
    return redirect('edit_post', slug=post.slug)