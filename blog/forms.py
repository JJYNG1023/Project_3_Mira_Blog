from django import forms
from .models import Comment, Post, CollaborationMessage

# Create comment form for users to submit comments on blog posts. The form is based on the Comment model and includes a single field for the content of the comment. The content field is rendered as a text input with specific CSS classes and a placeholder for better user experience. The label for the content field is set to an empty string to avoid displaying a label in the form.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content':forms.TextInput(attrs={
                'class':'post-comment-input',
                'placeholder':'Type comment',
            })
        }

        labels = {
            'content':'',
        }

#create post form for users to create new blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control rounded-0 border-dard',
                'placeholder': 'Title',}),
            'content': forms.Textarea(attrs={
                'class': 'form-control rounded-0 border-dard',
                'rows': 5,
                'placeholder': 'Content',}),
        }

#create post form for collaboration
class CollaborationForm(forms.ModelForm):
    class Meta:
        model = CollaborationMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control rounded-0 border-dark',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded-0 border-dark',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control rounded-0 border-dark',
                'rows': 4,
            }),
        }