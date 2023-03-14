from django.contrib import admin

from .models import GamePlaySession, WhiteList


admin.site.register(GamePlaySession)
admin.site.register(WhiteList)