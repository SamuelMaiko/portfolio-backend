from rest_framework import serializers
from a_aboutme.models import AboutMeInfo


class AboutMeInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMeInfo
        fields = [
            'id',
            'about_paragraph1',
            'about_paragraph2',
            'projects_completed',
            'years_of_experience',
            'created_at',
            'updated_at'
        ]
