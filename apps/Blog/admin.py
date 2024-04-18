from django.contrib import admin
from .models import Post, Comment, PostLike, CommentLike, Categories


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


admin.site.register(Comment)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(Categories)