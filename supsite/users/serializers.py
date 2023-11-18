# serializers.py
from rest_framework import serializers
from .models import User, Message, Issue

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title', 'body', 'timestamp', 'senior_id', 'junior_id', 'status')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role_id')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['body', 'issue_id', 'user_id']