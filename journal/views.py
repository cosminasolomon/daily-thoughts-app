from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Post


from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    
    

class OwnPostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user.id
        )
 
