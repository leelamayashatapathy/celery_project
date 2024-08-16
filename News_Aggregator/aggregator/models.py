from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=510)
    description = models.TextField()
    source = models.CharField(max_length=255)
    url = models.URLField()
    image = models.URLField(null=True,blank=True)
    published_at = models.DateTimeField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
