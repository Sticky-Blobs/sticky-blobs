from django.urls import path

from .views import GamePlayView, GamePlayViewDetail

urlpatterns = [
    path('gameplay', GamePlayView.as_view()),
    path('gameplay/<int:pk>', GamePlayViewDetail.as_view()),
]