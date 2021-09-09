from rest_framework import viewsets, permissions, generics
from .serializers import AccountSerializer, UserSerializer
from .models import Account

from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

