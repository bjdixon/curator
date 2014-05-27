from django.db import models
from django.utils import timezone


class Feed(models.Model):
    title = models.CharField(max_length=140)
    url = models.URLField()
    type_of_feed = models.ForeignKey(FeedTypes)
    last_checked = models.DateTimeField(default=timezone.now)


class FeedTypes(models.Model):
    name = models.CharField(max_length=140)
    html_id_or_class_containing_content = models.CharField(max_length=140)

