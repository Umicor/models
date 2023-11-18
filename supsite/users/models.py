from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role_id = models.IntegerField(default=1, validators=[
        MinValueValidator(1),  # Минимальное допустимое значение
        MaxValueValidator(2)  # Максимальное допустимое значение
    ])
    is_active = models.BooleanField(default=False)

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

class ActivationKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)
    # Использование primary_key=True для создания автоинкрементируемого id
    id = models.AutoField(primary_key=True)
