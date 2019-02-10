# Django's Libraries
from django.db import models


class NewsItem(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    date = models.CharField(
        max_length=144,
        blank=True,
        null=True
    )
    body = models.TextField(
        blank=True,
        null=True
    )
    actors = models.CharField(
        max_length=144,
        blank=True,
        null=True
    )
    place = models.CharField(
        max_length=144,
        blank=True,
        null=True
    )
    cover_img = models.URLField(
        max_length=500,
        blank=True,
        null=True
    )
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True
    )
