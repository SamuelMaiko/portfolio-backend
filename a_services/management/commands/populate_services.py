from django.core.management.base import BaseCommand
from a_services.models import Service, KeyFeature


class Command(BaseCommand):
    help = 'Populate services data'

    def handle(self, *args, **options):
        # Clear existing data
        Service.objects.all().delete()
        
        services_data = [
            {
                "title": "Web Development",
                "description": "Creating responsive, modern web applications using the latest technologies and best practices.",
                "category": "Frontend",
                "features": [
                    "React & Next.js",
                    "Responsive Design",
                    "Performance Optimization",
                    "SEO Friendly",
                ],
            },
            {
                "title": "Backend Development",
                "description": "Building robust server-side applications and APIs that scale with your business needs.",
                "category": "Backend",
                "features": [
                    "RESTful APIs",
                    "Database Integration",
                    "Authentication & Security",
                    "Cloud Deployment",
                ],
            },
            {
                "title": "Database Design",
                "description": "Designing efficient database structures and optimizing queries for maximum performance.",
                "category": "Database",
                "features": [
                    "Schema Design",
                    "Query Optimization",
                    "Data Migration",
                    "Performance Tuning",
                ],
            },
        ]

        for index, service_data in enumerate(services_data, 1):
            # Create service
            service = Service.objects.create(
                name=service_data["title"],
                badge=service_data["category"],
                description=service_data["description"],
                sequence=index
            )
            
            # Create key features for this service
            for feature_name in service_data["features"]:
                KeyFeature.objects.create(
                    service=service,
                    name=feature_name
                )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created service "{service.name}" with {len(service_data["features"])} key features'
                )
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {len(services_data)} services')
        )
