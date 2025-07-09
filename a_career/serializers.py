from rest_framework import serializers
from .models import Company, Career, CareerAchievement, CareerTechnology


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'location',
            'company_type',
            'created_at',
            'updated_at'
        ]


class CareerAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerAchievement
        fields = [
            'id',
            'achievement',
            'created_at',
            'updated_at'
        ]


class CareerTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerTechnology
        fields = [
            'id',
            'technology_name',
            'created_at',
            'updated_at'
        ]


class CareerSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    achievements = CareerAchievementSerializer(many=True, read_only=True)
    technologies = CareerTechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Career
        fields = [
            'id',
            'position',
            'company',
            'employment_type',
            'status',
            'start_date',
            'end_date',
            'description',
            'achievements',
            'technologies',
            'sequence',
            'created_at',
            'updated_at'
        ]
