from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите модуль настроек Django по умолчанию для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestHCS.config.settings')

app = Celery('TestHCS')

# Используйте строку здесь, чтобы рабочий узел всегда импортировал
# настройки Django при запуске.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузите модули задач из всех зарегистрированных Django-приложений.
app.autodiscover_tasks()
