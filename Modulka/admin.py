from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title',
		       'post_status','post_type','publish','post_modified')
    list_filter = ('post_status', 'publish')
    search_fields = ('post_title', 'post_content')
    prepopulated_fields = {'slug': ('post_title',)}
    raw_id_fields = ('post_author',)
    date_hierarchy = 'publish'
    ordering = ('post_status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'post', 'created', 'active') 
    list_filter = ('active', 'created', 'updated') 
    search_fields = ('name', 'email', 'body') 
