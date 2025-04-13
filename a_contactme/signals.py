from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReceivedEmail
from django.core.mail import EmailMessage
from django.conf import settings


@receiver(post_save, sender=ReceivedEmail)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        subject = f"New Message: {instance.subject}"
        message = f"From: {instance.sender_name} ({instance.sender_email})\n\n{instance.message}"

        email = EmailMessage(subject=subject,
                             body=message,
                             from_email=settings.EMAIL_HOST_USER,
                             to=[settings.WORK_EMAIL])

        email.send(fail_silently=True)
