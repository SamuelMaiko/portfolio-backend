from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReceivedEmail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def get_logo_url():
    """Get logo URL from settings or return None"""
    return getattr(settings, 'EMAIL_LOGO_URL', None)


@receiver(post_save, sender=ReceivedEmail)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        # Email subject
        subject = f"New Message: {instance.subject}" if instance.subject else "New Contact Message"

        # Context for the email template
        context = {
            'sender_name': instance.sender_name,
            'sender_email': instance.sender_email,
            'subject': instance.subject,
            'message': instance.message,
            'timestamp': instance.created_at,
            'logo_url': get_logo_url(),
        }

        # Render HTML and text templates
        html_content = render_to_string(
            'emails/contact_notification.html', context)
        text_content = render_to_string(
            'emails/contact_notification.txt', context)

        # Create email with both HTML and text versions
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.WORK_EMAIL]
        )

        # Attach HTML version
        email.attach_alternative(html_content, "text/html")

        # Send email
        email.send(fail_silently=True)
