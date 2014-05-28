from django.db import models
from django.utils import timezone
import bleach

from feed.models import Feed

attrs = {
    'a': ['href',],
    'img': ['src', 'alt',],
}

tags = (
    'h1', 'h2', 'h3', 'p', 'table', 'thead', 'tbody', 
    'th', 'tr', 'td', 'a', 'img', 'strong', 'em', 
    'br', 'ul', 'li',
)

class Item(models.Model):
    title = models.CharField(max_length=140)
    url = models.URLField()
    content = models.TextField()
    timestamp = models.DateTimeField()
    feed = models.ForeignKey(Feed)

    def save(self, *args, **kwargs):
        bleach.clean(self.content, tags=tags, attributes=attrs)
        super().save(*args, **kwargs)


