from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # This line is added to handle the /blog/ URL and render the same home view

    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    # This line is individual post detail view, which will display the details of a specific blog post based on its slug

    path('blog/<slug:slug>/like/', views.like_post, name='like_post'),
    # This line is added to handle the liking page

    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    # This line is added to handle the liking of comments

    path('blog/<slug:slug>/bookmark/', views.bookmark_post, name='bookmark_post'),
    # This line is added to handle the bookmarking of posts

    path('bookmarks/', views.bookmarked_posts, name='bookmarked_posts'),   
    # This line is added to handle the view for displaying all bookmarked posts for the authenticated user

    path('my-blog/', views.my_blog, name='my_blog'),
    # This line is added to handle the view for displaying posts created by the logged-in user

   # path('search/', views.search, name='search'),
    # This line is added to handle the search functionality at the /search/ URL

    path('create_post/', views.create_post, name='create_post'),
    # This line is added to handle the creation of new blog posts at the /create_post/ URL

    path('blog/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    # this line is added to handle the edit post function/view

    path('post-image/<int:image_id>/delete/', views.delete_post_image, name='delete_post_image'),
    # this line is added to delete existing post images in edit post mode.
]