from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a_aboutme.models import AboutMeInfo
from a_aboutme.serializers import AboutMeInfoSerializer

class AboutMeInfoView(APIView):
    def get(self, request):
        about_me_info = AboutMeInfo.objects.first()
        serializer = AboutMeInfoSerializer(about_me_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
