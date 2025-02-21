from apis.models import BaseModel
from django.db import models

class Project(BaseModel):
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=200)
    github_link = models.URLField(max_length=200)
    live_link = models.URLField(max_length=200)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.title
