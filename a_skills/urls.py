from django.urls import path
from a_skills.views import SkillAreasView

urlpatterns = [
    path('areas/', SkillAreasView.as_view(), name='skill-areas'),
]
