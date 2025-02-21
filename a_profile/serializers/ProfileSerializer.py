from rest_framework import serializers
from a_profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

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
            'resume', 
            'linkedin_url', 
            'github_url',
            'created_at',
            'updated_at'
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_resume(self, obj):
        request = self.context.get('request')
        if obj.resume and request:
            return request.build_absolute_uri(obj.resume.url)
        return None
