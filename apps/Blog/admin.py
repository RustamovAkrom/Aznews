from django.contrib import admin
from .models import Post, Comment, PostLike, CommentLike, Categories


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(Categories)