from rest_framework import serializers

from .models import GamePlaySession


class GamePlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlaySession
        fields = '__all__'