from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Issue, Message
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, MessageSerializer, IssueSerializer  #сериализатор пользователя
from rest_framework import status  # Добавлен импорт status
import json


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_data = serializers.serialize('json', users)
        return JsonResponse(user_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['POST'])
def create_issue(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = IssueSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'message': 'Issue created successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def get_issues(request):
    if request.method == 'GET':
        issues = Issue.objects.all()
        issue_data = serializers.serialize('json', issues)
        return JsonResponse(issue_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_issue(request, issue_id):
    if request.method == 'GET':
        try:
            issue = Issue.objects.get(pk=issue_id)
            issue_data = serializers.serialize('json', [issue])
            return JsonResponse(issue_data, safe=False)
        except Issue.DoesNotExist:
            return JsonResponse({'error': 'Issue not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET', 'POST'])
def get_message(request, issue_id):
    if request.method == 'GET':
        try:
            messages = Message.objects.filter(issue_id=issue_id)  # Используем filter для поиска сообщений по issue_id
            messages_data = serializers.serialize('json', messages)
            return JsonResponse(messages_data, safe=False)
        except Message.DoesNotExist:
            return JsonResponse({'error': 'Messages not found'}, status=404)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = MessageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

