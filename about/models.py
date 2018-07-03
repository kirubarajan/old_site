from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    github = models.URLField()
    link = models.URLField()
    users = models.CharField(max_length=50)

    class Meta:
        db_table = 'Project'