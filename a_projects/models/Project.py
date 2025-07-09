from apis.models import BaseModel
from django.db import models


class Project(BaseModel):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='project_pictures/')
    github_link = models.URLField(max_length=200, null=True, blank=True)
    live_link = models.URLField(max_length=200, null=True, blank=True)
    show_project = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.title
