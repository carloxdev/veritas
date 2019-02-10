# Django's Libraries
from django.contrib import admin

# Own's Libraries
from .models import NewsItem


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'body',
        'actors',
        'place',
        'cover_img',
        'link',
    )
    list_filter = ('date',)
    search_fields = (
        'title',
        'date',
        'body',
        'actors',
        'place',
        'cover_img',
        'link',
    )