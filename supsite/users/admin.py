from django.contrib import admin
from .models import Issue, User, Message

admin.site.register(Issue)
admin.site.register(User)
admin.site.register(Message)
