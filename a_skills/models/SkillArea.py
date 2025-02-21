from apis.models import BaseModel
from django.db import models

class SkillArea(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'skill_areas'

    def __str__(self):
        return self.name
