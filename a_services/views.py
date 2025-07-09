from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service
from .serializers import ServiceSerializer


class ServicesView(APIView):
    def get(self, request):
        """
        Get all services with their key features, ordered by sequence
        """
        try:
            services = Service.objects.all().order_by('sequence', 'name')
            serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': f'An error occurred while fetching services: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
