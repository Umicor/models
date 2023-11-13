from django.contrib import admin
from .models import Issue, User, Role, Message

admin.site.register(Issue)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Message)
