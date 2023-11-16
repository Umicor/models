from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Issue
from django.core import serializers

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role_id = request.POST.get('role_id')

        new_user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role_id=role_id
        )

        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_data = serializers.serialize('json', users)
        return JsonResponse(user_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_issue(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        timestamp = request.POST.get('timestamp')
        senior_id = request.POST.get('senior_id')
        junior_id = request.POST.get('junior_id')
        status = request.POST.get('status')

        new_issue = Issue.objects.create(
            title=title,
            body=body,
            timestamp=timestamp,
            senior_id=senior_id,
            junior_id=junior_id,
            status=status
        )

        return JsonResponse({'message': 'Issue created successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_issues(request):
    if request.method == 'GET':
        issues = Issue.objects.all()
        issue_data = serializers.serialize('json', issues)
        return JsonResponse(issue_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
