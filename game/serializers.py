from rest_framework import serializers

from .models import GamePlaySession, WhiteList


class GamePlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlaySession
        fields = '__all__'


class WhiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteList
        fields = '__all__'