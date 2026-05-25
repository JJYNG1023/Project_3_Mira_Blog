from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # This line is added to handle the /blog/ URL and render the same home view

    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    # This line is individual post detail view, which will display the details of a specific blog post based on its slug

    path('blog/<slug:slug>/like/', views.like_post, name='like_post'),
    # This line is added to handle the liking page

   # path('comment/<int:post_id>/edit/', views.edit_comment, name='edit_comment'),
    # This line is added to handle the editing of comments for a specific post based on its ID

    #path('comment/<int:post_id>/delete/', views.delete_comment, name='delete_comment'),
    # This line is added to handle the deletion of comments for a specific post based on its ID

   # path('blog/', views.home, name='blog'), 
    # This line is added to handle the /blog/ URL and render the same home view

   # path('blog/', views.post_list, name='post_detail'),
    # This displays the list of blog posts at the /blog/ URL

   # path('search/', views.search, name='search'),
    # This line is added to handle the search functionality at the /search/ URL

   # path('create_post/', views.create_post, name='create_post'),
    # This line is added to handle the creation of new blog posts at the /create_post/ URL

   # path('profile/', views.profile, name='profile'),
    # This line is added to handle the user profile view at the /profile/ URL

   # path('notifications/', views.notifications, name='notifications'),
    # This line is added to handle the notifications view at the /notifications/ URL
]