from rest_framework import serializers
from .models import Institution, Education, EducationSkill


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = [
            'id',
            'name',
            'location',
            'created_at',
            'updated_at'
        ]


class EducationSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSkill
        fields = [
            'id',
            'skill_name',
            'created_at',
            'updated_at'
        ]


class EducationSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    skills = EducationSkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Education
        fields = [
            'id',
            'title',
            'education_type',
            'institution',
            'status',
            'start_date',
            'end_date',
            'description',
            'skills',
            'created_at',
            'updated_at'
        ]
