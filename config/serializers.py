from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'url']
        
class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    application = ApplicationSerializer(read_only=True)
    application_id = serializers.PrimaryKeyRelatedField(
        queryset=Application.objects.all(), source='application', write_only=True)

    class Meta:
        model = Task
        fields = ['id', 'user', 'name', 'task_description', 'application', 'application_id', 'status', 'deadline']