# serializers.py in your app directory

from rest_framework import serializers
from .models import *
from config.serializers import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'members']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'content', 'group', 'timestamp', 'file']
