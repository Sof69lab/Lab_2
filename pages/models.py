from django.db import models

class Message(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()

