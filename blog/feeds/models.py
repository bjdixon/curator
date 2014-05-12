from django.db import models
from django.utils import timezone


FEED_TYPES = (
	('News', 'News'), 
	('Youtube', 'Youtube'),
)


class Feed(models.Model):
	title = models.CharField(max_length=140)
	url = models.URLField()
	type_of_feed = models.CharField(max_length=32, choices=FEED_TYPES)
	last_checked = models.DateTimeField(default=timezone.now)


