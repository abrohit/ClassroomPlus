from django.db import models
from django.contrib.auth.models import User

class Sessions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sessions = models.TextField(blank=True)
