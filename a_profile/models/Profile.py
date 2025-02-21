from apis.models import BaseModel
from django.db import models

class Profile(BaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    resume_url = models.URLField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    linkedin_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return self.name
