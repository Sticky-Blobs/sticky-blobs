from django.urls import path

from .views import GamePlayView, GamePlayViewDetail, WhiteListView

urlpatterns = [
    path('gameplay', GamePlayView.as_view()),
    path('gameplay/<int:pk>', GamePlayViewDetail.as_view()),
    path('whitelist', WhiteListView.as_view()),
    path('whitelist/<int:pk>', WhiteListView.as_view())
]