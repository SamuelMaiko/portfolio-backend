from rest_framework import serializers
from a_skills.models import SkillArea
from .LanguageSerializer import LanguageSerializer

class SkillAreaSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = SkillArea
        fields = [
            'id',
            'name',
            'description',
            'languages',
            'created_at',
            'updated_at'
        ]
