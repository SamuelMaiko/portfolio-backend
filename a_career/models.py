from django.db import models
from apis.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    # e.g., "Startup", "Corporation"
    company_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Career(BaseModel):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
    ]

    STATUS_CHOICES = [
        ('current', 'Current'),
        ('completed', 'Completed'),
    ]

    position = models.CharField(max_length=255)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='careers')
    employment_type = models.CharField(
        max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='completed')
    # Flexible format like "Jan 2024"
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(
        max_length=50, null=True, blank=True)  # Flexible format
    description = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(default=0)

    class Meta:
        db_table = 'careers'

    def __str__(self):
        return f"{self.position} at {self.company.name}"


class CareerAchievement(BaseModel):
    career = models.ForeignKey(
        Career, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.TextField()

    class Meta:
        db_table = 'career_achievements'

    def __str__(self):
        return f"Achievement for {self.career.position}"


class CareerTechnology(BaseModel):
    career = models.ForeignKey(
        Career, on_delete=models.CASCADE, related_name='technologies')
    technology_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'career_technologies'

    def __str__(self):
        return f"{self.technology_name} - {self.career.position}"
