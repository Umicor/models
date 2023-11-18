from django.contrib import admin
from .models import Issue, User, Message, ActivationKey

admin.site.register(Issue)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(ActivationKey)