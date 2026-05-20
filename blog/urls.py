from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.home, name='blog'), 
    # This line is added to handle the /blog/ URL and render the same home view

    path('blog/', views.post_list, name='post_detail'),
    # This displays the list of blog posts at the /blog/ URL

    path('blog/<slug:slug>/', views.post_detail, name='new_post'),
    # This line is individual post detail view, which will display the details of a specific blog post based on its slug
]