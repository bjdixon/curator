from django.db import models
from django.utils import timezone

from items.models import Item


class Article(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField()
    content = models.TextField()
    timestamp = models.DateTimeField()

