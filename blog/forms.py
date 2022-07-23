"""
Forms imports
"""
from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    returns comments
    """
    class Meta:
        """
        returns comment
        """
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Form to add a blog post
    """
    class Meta:
        """
        method to return form details
        """
        model = Post
        fields = (
            'title',
            'location',
            'excerpt',
            'featured_image',
            'content',
            'distance',
            'time',
            'difficulty',
        )

        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
