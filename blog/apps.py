'''
    imports
'''
from django.apps import AppConfig


class BlogConfig(AppConfig):
    '''
        class to define app name
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
