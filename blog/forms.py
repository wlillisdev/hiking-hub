from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Form to add a blog post
    """
    class Meta:
        model = Post
        fields = (
            'title',
            # 'slug',
            'location',
            'excerpt',
            'featured_image',
            'content',
            'distance',
            'time',
            'difficulty',
            # 'status',
        )

        # widgets = {
        #     'content': SummernoteWidget(),
        # }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

# class PostForm(forms.ModelForm):
#     class meta:
#         model = Post
#         fields = ('title', 'location', 'authour', 'excerpt',
#          'featured_image', 'content', 'distance', 'time', 'difficulty')
        
#         widget = {
#             'title': form.TextInput(attrs={'class': 'form-control'}),
#             'location': form.TextInput(attrs={'class': 'form-control'}),  
#             'authour': form.Select(attrs={'class': 'form-control'}),  
#             'excerpt': form.Textarea(attrs={'class': 'form-control'}),  
#             'featured_image': form.Image(attrs={'class': 'form-control'}),
#             'content': form.Textarea(attrs={'class': 'form-control'}),
#             'distance': form.TextInput(attrs={'class': 'form-control'}),
#             'time': form.TextInput(attrs={'class':'form-control'}),
#             'difficulty': form.TextInput(attrs={'class': 'form-control'}),        
#         }