from rest_framework import serializers
from a_projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'category',
            'description',
            'image',
            'github_link',
            'live_link',
            'show_project',
            'sequence',
            'created_at',
            'updated_at'
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
