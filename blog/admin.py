from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register Post models.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content')

