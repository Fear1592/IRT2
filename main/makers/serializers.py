from rest_framework import serializers
from .models import Produced, Images


class ProducedDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = Produced
        fields = ('__all__')


class ProducedListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = Produced
        fields = ['user']
