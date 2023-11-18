from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.core.mail import send_mail

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


@receiver(post_save, sender=User)
def create_activation_key_send_email(sender, instance, created, **kwargs):
    if created:
        unique_id = uuid.uuid4()
        hex_unique_id = unique_id.hex
        ActivationKey.objects.create(user=instance, key=hex_unique_id)

        send_mail(
            'Account user',
            f'your uuid{hex_unique_id}',
            'fogotstop@gmail.com',
            [User.email],
            fail_silently=True,
        )


