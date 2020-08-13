from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username', 'email','last_login','is_active')
