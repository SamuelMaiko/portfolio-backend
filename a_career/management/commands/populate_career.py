from django.core.management.base import BaseCommand
from a_career.models import Company, Career, CareerAchievement, CareerTechnology


class Command(BaseCommand):
    help = 'Populate career data with sample data'

    def handle(self, *args, **options):
        # Create company
        duka_tech, created = Company.objects.get_or_create(
            name="Duka Technologies",
            defaults={
                'location': 'Nairobi, Kenya',
                'company_type': 'Startup'
            }
        )

        # Create career entry
        software_dev_intern, created = Career.objects.get_or_create(
            position="Software Developer Intern",
            company=duka_tech,
            defaults={
                'employment_type': 'internship',
                'status': 'completed',
                'start_date': 'Jan 2024',
                'end_date': 'Apr 2024',
                'description': 'Contributed to full-stack development, including database design, frontend interfaces, and backend APIs for startup products.'
            }
        )

        # Create achievements
        achievements = [
            'Designed and optimized PostgreSQL database schemas for performance and scalability',
            'Contributed to building and deploying a production-ready backend API for mobile integration'
        ]

        for achievement_text in achievements:
            CareerAchievement.objects.get_or_create(
                career=software_dev_intern,
                achievement=achievement_text
            )

        # Create technologies used
        technologies = [
            'React',
            'Django',
            'PostgreSQL'
        ]

        for tech_name in technologies:
            CareerTechnology.objects.get_or_create(
                career=software_dev_intern,
                technology_name=tech_name
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated career data')
        )
