from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role_id = models.IntegerField()


class Role(models.Model):
    value = models.CharField(max_length=20)

class Issue(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=250)
    timestamp = models.TimeField()
    senior_id = models.IntegerField()
    junior_id = models.IntegerField()
    status = models.CharField(max_length=20)

class Message(models.Model):
    body = models.CharField(max_length=200)
    issue_id = models.IntegerField()
    user_id = models.IntegerField()