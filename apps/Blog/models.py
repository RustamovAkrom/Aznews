from apps.shared.models import AbstractBaseModel
from apps.users.models import User
from django.db import models


class Categories(AbstractBaseModel):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "categori"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
    
class Tag(AbstractBaseModel):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return self.name
    

class Post(AbstractBaseModel):
    user = models.ForeignKey(User, models.CASCADE, related_name="posts")
    title = models.CharField(max_length=120)
    descriptions = models.CharField(max_length=180, blank=True, null=True)
    content = models.TextField()
    categories = models.ForeignKey(Categories, models.CASCADE, related_name="posts")
    tags = models.ForeignKey(Tag, models.CASCADE, related_name="posts")
    content_image = models.ImageField(upload_to="posts/content/images/")
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return self.title
    
    
class Comment(AbstractBaseModel):
    post = models.ForeignKey(Post, models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, models.CASCADE, related_name="comments")
    message = models.TextField()
    reply = models.ManyToManyField(User, related_name="reply_comments", blank=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        if self.reply is not None:
            return f"{self.user} -> {self.reply}"
        else:
            return f"{self.user} -> {self.post}"


class CommentLike(AbstractBaseModel):
    comment = models.ForeignKey(Comment, models.DO_NOTHING, related_name="comment_likes")
    user = models.ForeignKey(User, models.CASCADE, related_name="comment_likes")

    class Meta:
        verbose_name = "comment_like"
        verbose_name_plural = "Comment Likes"

    def like_count(self):
        return self.user.objects.count()
    
    def __str__(self) -> str:
        return f"{self.user} - like comment -> {self.comment}"
    

class PostLike(AbstractBaseModel):
    post = models.ForeignKey(Post, models.DO_NOTHING, related_name="post_likes")
    user = models.ForeignKey(User, models.CASCADE, related_name="post_likes")

    class Meta:
        verbose_name = "post_like"
        verbose_name_plural = "Post Likes"

    @property
    def liek_count(self):
        return self.user.objects.count()

    def __str__(self) -> str:
        return f"{self.user} - like post -> {self.post}"
    