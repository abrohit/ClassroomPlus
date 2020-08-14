from django.shortcuts import render
from rest_framework import viewsets
from django.db import models
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all().order_by('id')
    serializer_class = UserSerializer
