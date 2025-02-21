from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a_profile.models import Profile
from a_profile.serializers import ProfileSerializer

class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.first()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
