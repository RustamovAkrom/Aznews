from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Pictures(AbstractBaseModel):
    image = models.ImageField(upload_to="images/")
    descriptions = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        verbose_name = "pictures"
        verbose_name_plural = "Pictures"

    def __str__(self) -> str:
        return self.image.url


class YouTubeVideoUrl(AbstractBaseModel):
    url = models.URLField()
    title = models.CharField(max_length=80)
    descriptions = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "youtube_video"
        verbose_name_plural = "YouTube Videos"

    def __str__(self) -> str:
        return self.title


class AnonimusUserEmails(AbstractBaseModel):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "anonimus_user_emails"
        verbose_name_plural = "Anonimus User Emails"

    def __str__(self) -> str:
        return self.email
