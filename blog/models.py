from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    bulma_color = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Category'

class Post(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    recommended = models.BooleanField(default=False)

    class Meta:
        db_table = 'Post'