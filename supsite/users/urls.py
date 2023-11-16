from django.urls import path
from .views import create_user, get_users, create_issue, get_issues, get_issue

urlpatterns = [
    path('users/create/', create_user, name='create-user'),
    path('users/', get_users, name='get-users'),
    path('issues/create/', create_issue, name='create-issue'),
    path('issues/', get_issues, name='get-issues'),
    path('issues/<int:issue_id>/', get_issue, name='get-issue'),
]