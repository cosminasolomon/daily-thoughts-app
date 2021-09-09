
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Post
from django.contrib.auth.models import User


from journal import models

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['author']


    def create(self, validated_data):
        author = self.context['request'].user
        post = Post.objects.create(author=author, **validated_data)
        return post

class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = "__all__"
