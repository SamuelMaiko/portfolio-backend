from apis.models import BaseModel
from django.db import models

class ReceivedEmail(BaseModel):
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        db_table = 'received_emails'

    def __str__(self):
        return f"{self.subject} from {self.sender_name}"
 