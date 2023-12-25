from django.contrib import admin
from pages.models import Message
from django.contrib.admin.models import LogEntry

admin.site.register(Message)
admin.site.register(LogEntry)
