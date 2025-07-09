from apis.models import BaseModel
from django.db import models


class AboutMeInfo(BaseModel):
    about_paragraph1 = models.TextField(default="")
    about_paragraph2 = models.TextField(default="")
    projects_completed = models.IntegerField(default=0)
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        db_table = 'about_me_info'

    def __str__(self):
        return self.about_paragraph1[:50]
