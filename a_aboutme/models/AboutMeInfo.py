from apis.models import BaseModel
from django.db import models

class AboutMeInfo(BaseModel):
    photo_url = models.ImageField(upload_to='media/about_me_picture')
    description = models.TextField()

    class Meta: 
        db_table = 'about_me_info'

    def __str__(self):
        return self.description[:50]   
