from django.core.management.base import BaseCommand
from a_education.models import Institution, Education, EducationSkill


class Command(BaseCommand):
    help = 'Populate education data with sample data'

    def handle(self, *args, **options):
        # Create institutions
        kenyatta_uni, created = Institution.objects.get_or_create(
            name="Kenyatta University",
            defaults={'location': 'Kenya'}
        )
        
        moringa_school, created = Institution.objects.get_or_create(
            name="Moringa School",
            defaults={'location': 'Kenya'}
        )

        # Create education entries
        bachelor_cs, created = Education.objects.get_or_create(
            title="Bachelor of Computer Science",
            defaults={
                'education_type': 'degree',
                'institution': kenyatta_uni,
                'status': 'ongoing',
                'start_date': '2022',
                'end_date': '2026',
                'description': 'Focused on core computer science subjects including data structures, algorithms, databases, operating systems, and computer architecture.'
            }
        )

        certificate_se, created = Education.objects.get_or_create(
            title="Certificate of Software Engineering",
            defaults={
                'education_type': 'certificate',
                'institution': moringa_school,
                'status': 'completed',
                'start_date': 'May 29 2023',
                'end_date': '17 Nov 2023',
                'description': 'Fast-paced 6-month bootcamp covering JavaScript, React.js, Flask, and SQLAlchemy. Built weekly solo projects and monthly group projects under mentor guidance with regular evaluations.'
            }
        )

        # Create skills for Bachelor's degree
        bachelor_skills = [
            'Database Systems',
            'Data Structures & Algorithms',
            'Artificial Intelligence',
            'Operating Systems'
        ]

        for skill_name in bachelor_skills:
            EducationSkill.objects.get_or_create(
                education=bachelor_cs,
                skill_name=skill_name
            )

        # Create skills for Certificate
        certificate_skills = [
            'Team work & collaboration',
            'React JS',
            'Algorithm analysis',
            'System design fundamentals'
        ]

        for skill_name in certificate_skills:
            EducationSkill.objects.get_or_create(
                education=certificate_se,
                skill_name=skill_name
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated education data')
        )
