from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import dateparse, timezone

from .models import GamePlaySession, WhiteList
from .serializers import GamePlaySerializer, WhiteListSerializer
from .permissions import IsAdminOrRetrieveOnly

class GamePlayView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = GamePlaySession.objects.all()
    serializer_class = GamePlaySerializer


class GamePlayViewDetail(APIView):
    permission_classes = (IsAdminOrRetrieveOnly,)
    def get(self, request, pk):
        game_play = get_object_or_404(GamePlaySession, pk=pk)
        serializer = GamePlaySerializer(game_play)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = request.data
        game_play = get_object_or_404(GamePlaySession, pk=pk)
        serializer = GamePlaySerializer(game_play, data, partial=True)
        serializer.is_valid(raise_exception=True)
        start_time = game_play.start_time

        time_data = serializer.validated_data.get("end_time")
        end_time = dateparse.parse_datetime(time_data)

        if not end_time:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        end_time = timezone.make_aware(end_time)
        total_game_time = end_time - start_time
        game_play.total_game_time = total_game_time
        game_play.save(update_fields=["total_game_time"])
        serializer.save()
        return Response(serializer.data)
    

class WhiteListView(generics.ListCreateAPIView):
    queryset = WhiteList.objects.all()
    serializer_class = WhiteListSerializer()
    

class WhiteListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrRetrieveOnly)
    queryset = WhiteList.objects.all()
    serializer_class = WhiteListSerializer
