from django.db import models
from apis.models.BaseModel import BaseModel

class SaccoAppUpdate(BaseModel):
    version_name = models.CharField(max_length=50, unique=True) # e.g. 1.3.0
    apk_file = models.FileField(upload_to='sacco_updates/')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = "Sacco App Update"
        verbose_name_plural = "Sacco App Updates"
        ordering = ['-created_at']
