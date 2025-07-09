from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone
from a_contactme.signals import get_logo_url


class Command(BaseCommand):
    help = 'Test the email template rendering'

    def handle(self, *args, **options):
        # Sample context data
        context = {
            'sender_name': 'John Doe',
            'sender_email': 'johndoe@gmail.com',
            'subject': 'Website Quotation Request',
            'message': 'I would like quotation for building a website. Thank you so much',
            'timestamp': timezone.now(),
            'logo_url': get_logo_url(),
        }
        
        try:
            # Render HTML template
            html_content = render_to_string('emails/contact_notification.html', context)
            
            # Render text template
            text_content = render_to_string('emails/contact_notification.txt', context)
            
            self.stdout.write(
                self.style.SUCCESS('✅ Email templates rendered successfully!')
            )
            
            self.stdout.write("\n" + "="*50)
            self.stdout.write("HTML TEMPLATE PREVIEW:")
            self.stdout.write("="*50)
            self.stdout.write(html_content[:500] + "..." if len(html_content) > 500 else html_content)
            
            self.stdout.write("\n" + "="*50)
            self.stdout.write("TEXT TEMPLATE PREVIEW:")
            self.stdout.write("="*50)
            self.stdout.write(text_content)
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error rendering templates: {str(e)}')
            )
