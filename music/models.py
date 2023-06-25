from django.db import models
from django.contrib.auth.models import User

class private_file_name(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        file_name = models.CharField(max_length=40)
class public(models.Model):
        file_name = models.CharField(max_length=40)
class protected_file_name(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        file_name = models.CharField(max_length=40)
