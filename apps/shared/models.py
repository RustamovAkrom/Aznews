from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Pictures(AbstractBaseModel):
    image = models.ImageField(upload_to="images/")
    descriptions = models.CharField(max_length=180)

    class Meta:
        verbose_name = "pictures"
        verbose_name_plural = "Pictures"
        

    def __str__(self) -> str:
        return self.image
    

class YouTubeVideoUrl(AbstractBaseModel):
    url = models.URLField()
    title = models.CharField(max_length=80)
    descriptions = models.CharField(max_length=300)

    class Meta:
        verbose_name = "youtube_video"
        verbose_name_plural = "YouTube Videos"

    def __str__(self) -> str:
        return self.title
    