from rest_framework import serializers

from server.models import Illumination


class IlluminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illumination
        fields = ['id', 'level', 'created_at', 'illumination_class']
        read_only_fields = ['id', 'created_at']