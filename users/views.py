from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.encoding import force_bytes, force_str
from django.utils.http import (urlsafe_base64_decode, urlsafe_base64_encode)
from django.contrib.sites.shortcuts import get_current_site
from django.db import transaction

from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .models import User
from helpers.utils import account_activation_token, send_verification_mail


class RegisterView(APIView):
    permission_classes =(permissions.AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.save()

        current_site = get_current_site(request)
        verification_link = 'http://{}/account-activation/{}/{}'.format(
            current_site.domain, urlsafe_base64_encode(
            force_bytes(user_instance.pk)), account_activation_token.make_token(user_instance))
        print('Account verification link: %s' % verification_link)
        send_verification_mail(
            user_instance.email, verification_link)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

def account_activation(request, uidb64, token):
    """
    Email Activation

    Endpoint for verifying emails
    """
    with transaction.atomic():
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            # if not Wallet.objects.filter(user__pk=user.pk).exists():
            #     Wallet.objects.create(user=user)
            return HttpResponseRedirect("https://stickyblobs.com")
        else:
            return HttpResponse(
                'Activation link is invalid or account already activated')


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer