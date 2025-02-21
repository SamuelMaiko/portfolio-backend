from rest_framework import serializers
from a_aboutme.models import AboutMeInfo

class AboutMeInfoSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = AboutMeInfo
        fields = [
            'id',
            'photo',
            'description',
            'created_at',
            'updated_at'
        ]

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None
