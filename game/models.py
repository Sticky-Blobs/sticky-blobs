from django.db import models

from users.models import User

class GamePlaySession(models.Model):
    user = models.ForeignKey(User, related_name='game_time_user', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    total_game_time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user} | {self.start_time}"
    
class WhiteList(models.Model):
    wallet_address = models.CharField(max_length=500, unique=True)
    faction_choice = models.CharField(max_length=100)