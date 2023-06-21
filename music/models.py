from django.db import models
from django.contrib.auth.models import User

class music_user(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        real_name=models.CharField(max_length=40)
