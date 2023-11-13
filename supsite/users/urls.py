from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import get_all_users, create_user, create_issue, get_all_issues
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('allusers/', get_all_users, name='get_all_users'),
    path('createusers/', create_user, name='create_user'),
    path('createissue/', create_issue, name='create_issue'),
    path('allissues', get_all_issues, name='get_all_issues'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
