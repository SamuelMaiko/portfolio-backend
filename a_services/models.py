from django.db import models
from apis.models import BaseModel


class Service(BaseModel):
    badge = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(default=0)

    class Meta:
        db_table = 'services'

    def __str__(self):
        return self.name


class KeyFeature(BaseModel):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='keyfeatures')
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'key_features'

    def __str__(self):
        return f"{self.name} - {self.service.name}"
