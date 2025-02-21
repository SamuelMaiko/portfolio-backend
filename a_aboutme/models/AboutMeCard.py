from apis.models import BaseModel
from django.db import models

class AboutMeCard(BaseModel):
    title = models.CharField(max_length=255)
    lineOne = models.CharField(max_length=255)
    lineTwo = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)

    class Meta:
        db_table = 'about_me_cards'

    def __str__(self):
        return self.title
