from rest_framework import serializers
from a_contactme.models import ReceivedEmail

class ReceivedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedEmail
        fields = [
            'id',
            'sender_name',
            'sender_email',
            'subject',
            'message'
            'created_at',
            'updated_at',
        ]
