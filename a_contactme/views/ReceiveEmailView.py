from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a_contactme.serializers import ReceivedEmailSerializer

class ReceiveEmailView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReceivedEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
