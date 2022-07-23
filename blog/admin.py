'''
    imports admin.py
'''
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register Post models.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
        Class to control what will be shown on posts
    '''
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
        Class to show what is will be shown in comments
    '''
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        '''
            method so comments need to be approved before publishing
        '''
        queryset.update(approved=True)
