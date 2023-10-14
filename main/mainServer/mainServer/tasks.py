# myapp/tasks.py
# myapp/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.sites.models import Site

@shared_task
def my_scheduled_task():
    # 이곳에 주기적으로 실행할 작업을 작성
    current_site = Site.objects.get_current()
    send_mail('주기적인 작업 실행', f'사이트: {current_site}', 'sender@example.com', ['recipient@example.com'], fail_silently=False)
