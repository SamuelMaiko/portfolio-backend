from rest_framework import serializers
from a_aboutme.models import AboutMeCard

class AboutMeCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeCard
        fields = [
            'id',
            'title',
            'lineOne',
            'lineTwo',
            'institution',
            'created_at',
            'updated_at'
        ]
