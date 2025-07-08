from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Import models
from a_profile.models import Profile
from a_aboutme.models import AboutMeInfo
from a_skills.models import SkillArea
from a_projects.models import Project
from a_education.models import Education
from a_career.models import Career

# Import serializers
from a_profile.serializers import ProfileSerializer
from a_aboutme.serializers import AboutMeInfoSerializer
from a_skills.serializers import SkillAreaSerializer
from a_projects.serializers import ProjectSerializer
from a_education.serializers import EducationSerializer
from a_career.serializers import CareerSerializer


class PortfolioView(APIView):
    def get(self, request):
        """
        Aggregates all portfolio data from different endpoints into a single response
        """
        try:
            # Get profile data
            profile = Profile.objects.first()
            profile_data = ProfileSerializer(
                profile, context={"request": request}).data if profile else None

            # Get about me info
            about_me_info = AboutMeInfo.objects.first()
            about_me_info_data = AboutMeInfoSerializer(
                about_me_info, context={'request': request}).data if about_me_info else None

            # Get skill areas with languages
            skill_areas = SkillArea.objects.all()
            skill_areas_data = SkillAreaSerializer(skill_areas, many=True).data

            # Get projects
            projects = Project.objects.all()
            projects_data = ProjectSerializer(
                projects, many=True, context={'request': request}).data

            # Get education data
            educations = Education.objects.all()
            education_data = EducationSerializer(educations, many=True).data

            # Get career data
            careers = Career.objects.all()
            career_data = CareerSerializer(careers, many=True).data

            # Aggregate all data
            portfolio_data = {
                'profile': profile_data,
                'about_me': about_me_info_data,
                'skills': skill_areas_data,
                'projects': projects_data,
                'education': education_data,
                'careers': career_data
            }

            return Response(portfolio_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'An error occurred while fetching portfolio data: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
