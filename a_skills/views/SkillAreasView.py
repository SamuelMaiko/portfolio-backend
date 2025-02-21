from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a_skills.models import SkillArea
from a_skills.serializers import SkillAreaSerializer

class SkillAreasView(APIView):
    def get(self, request):
        skill_areas = SkillArea.objects.all()
        serializer = SkillAreaSerializer(skill_areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
