from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a_aboutme.models import AboutMeCard
from a_aboutme.serializers.AboutMeCardSerializer import AboutMeCardSerializer

class AboutMeCardsView(APIView):
    def get(self, request):
        about_me_cards = AboutMeCard.objects.all()
        serializer = AboutMeCardSerializer(about_me_cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
