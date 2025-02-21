from apis.models import BaseModel
from django.db import models

class Profile(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/profile_picture', null=True, blank=True)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    resume = models.FileField(upload_to='media/resume', null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)
    github_url = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return self.name
