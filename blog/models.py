from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Category'

class Post(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()
    category = models.OneToOneField(Category, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Post'