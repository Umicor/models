# serializers.py
from rest_framework import serializers
from .models import User, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role_id')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['body', 'issue_id', 'user_id']