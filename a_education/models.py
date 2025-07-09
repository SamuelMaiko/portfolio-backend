from django.db import models
from apis.models import BaseModel


class Institution(BaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'institutions'

    def __str__(self):
        return self.name


class Education(BaseModel):
    EDUCATION_TYPE_CHOICES = [
        ('degree', 'Degree'),
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('course', 'Course'),
    ]

    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('paused', 'Paused'),
    ]

    title = models.CharField(max_length=255)
    education_type = models.CharField(
        max_length=20, choices=EDUCATION_TYPE_CHOICES)
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name='educations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # Flexible format like "2022" or "May 29 2023"
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(
        max_length=50, null=True, blank=True)  # Flexible format
    description = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(default=0)

    class Meta:
        db_table = 'educations'

    def __str__(self):
        return f"{self.title} - {self.institution.name}"


class EducationSkill(BaseModel):
    education = models.ForeignKey(
        Education, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'education_skills'

    def __str__(self):
        return f"{self.skill_name} - {self.education.title}"
