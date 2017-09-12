from django.db import models


class Article(models.Model):
    """
    Model representing news articles
    """
    title = models.CharField(max_length=200, help_text="Article title")
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.title
