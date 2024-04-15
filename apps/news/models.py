from django.db import models
from apps.shared.models import AbstractBaseModel
from apps.users.models import User


class Catgoriyes(AbstractBaseModel):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name


class Subjects(AbstractBaseModel):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "subject"
        verbose_name_plural = "subjects"
    
    def __str__(self) -> str:
        return self.name
    

class News(AbstractBaseModel):
    image = models.ImageField(upload_to="news/images/")
    title = models.CharField(max_length=120)
    descriptions = models.TextField(blank=True, null=True)
    content = models.TextField()
    categories = models.ForeignKey(Catgoriyes, on_delete=models.CASCADE, related_name="news")
    subjects = models.ForeignKey(Subjects, models.CASCADE, related_name="news")
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "new"
        verbose_name = "news"

    def __str__(self) -> str:
        return self.title


class Pictures(AbstractBaseModel):
    image = models.ImageField(upload_to="images/")
    descriptions = models.CharField(max_length=180)

    class Meta:
        verbose_name_plural = "picture"
        verbose_name = "pictures"

    def __str__(self) -> str:
        return self.image
    
    
class Contact(AbstractBaseModel):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "contact"
        verbose_name = "contacts"

    def __str__(self) -> str:
        return self.name
    

class Comment(AbstractBaseModel):
    news = models.ForeignKey(News, models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, models.DO_NOTHING, related_name="comments")
    comment = models.TextField()

    reply = models.ManyToManyField(User, related_name="reply_comments", blank=True)

    class Meta:
        verbose_name_plural = "comment"
        verbose_name = "comments"

    def reply_to(self, user):
        self.reply.add(user)

    @property
    def comment_count(self):
        return self.comment.count()

    def __str__(self) -> str:
        if self.reply is not None:
            return f"{self.user} -> {self.reply}"
        else:
            return f"{self.user} -> {self.news}"
    