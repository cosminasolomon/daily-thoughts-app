from django.db.models import fields

from rest_framework import serializers
from journal.serializers import PostSerializer
from journal import models
from .models import Account
from journal.models import Post
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}
        


    def create(self, validated_data):
        
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# class AdminUsersSerializer(serializers.ModelSerializer):
#     post = PostSerializer(read_only=True)
#     class Meta:
#         model = User
#         fields = "__all__"