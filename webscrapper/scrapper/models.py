from django.db import models

from django.db import models

class ImdbNews(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image  = models.URLField(null=True,blank=True)
    external_link = models.URLField(null=True,blank=True)

class Info(models.Model):
    info = models.CharField(max_length=1000)

    
