
from django.db import models
from django.contrib.auth.models import User

# from users.models import Post
# from django.contrib.auth import authenticate, login

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    
    def _str_(self):
        return self.name

# class AccountJournal(models.Model):
#     journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True )
#     def _str_(self):
#         return self