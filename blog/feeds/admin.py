from django.contrib import admin
from . import models


class FeedAdmin(admin.ModelAdmin):
	pass


admin.site.register(models.Feed, FeedAdmin)
