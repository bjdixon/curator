from django.contrib import admin
from . import models


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Item, ItemAdmin)
