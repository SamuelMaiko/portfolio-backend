from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a_projects.models import Project
from a_projects.serializers import ProjectSerializer

class ProjectsListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
