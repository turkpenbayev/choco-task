from celery import shared_task

from choco.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@shared_task
def notify_user(subject, message, email):
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [email])
        return email
    except Exception as ex:
        return email
        
        