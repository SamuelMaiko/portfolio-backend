from rest_framework import serializers
from a_skills.models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'id',
            'name',
            'level',
            'created_at',
            'updated_at'
        ]
