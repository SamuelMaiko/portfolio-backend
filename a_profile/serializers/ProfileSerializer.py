from rest_framework import serializers
from a_profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 
            'name', 
            'image', 
            'position', 
            'phone', 
            'email', 
            'location', 
            'resume_url', 
            'linkedin_url', 
            'github_url',
            'created_at',
            'updated_at'
        ]
