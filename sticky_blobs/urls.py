from django.contrib import admin
from django.urls import path, include

from users.views import account_activation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('game/', include('game.urls')),

    path('account-activation/<uidb64>/<token>',
         account_activation, name='account_activation'),
]
