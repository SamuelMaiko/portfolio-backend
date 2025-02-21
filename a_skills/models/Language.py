from apis.models import BaseModel
from django.db import models
from .SkillArea import SkillArea

class Language(BaseModel):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    skill_area = models.ForeignKey(SkillArea, related_name='languages', on_delete=models.CASCADE)

    class Meta:
        db_table = 'languages'

    def __str__(self):
        return self.name
