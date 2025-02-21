from rest_framework import serializers
from a_projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description', 
            'image',
            'github_link',
            'live_link',
            'created_at',
            'updated_at'
        ]
