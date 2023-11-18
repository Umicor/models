from django.core.mail import send_mail
from supsite.supsite.celery import celery_app

@celery_app.task()
def send_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
