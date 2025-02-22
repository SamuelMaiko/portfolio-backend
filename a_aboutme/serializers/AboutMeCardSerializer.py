from rest_framework import serializers
from a_aboutme.models import AboutMeCard

class AboutMeCardSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = AboutMeCard
        fields = [
            'id',
            'icon',
            'title',
            'lineOne',
            'lineTwo',
            'institution',
            'created_at',
            'updated_at'
        ]

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon and request:
            return request.build_absolute_uri(obj.icon.url)
        return None
