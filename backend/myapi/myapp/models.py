from django.db import models

class ToDo(models.Model):
    description = models.CharField(max_length=50)
    completed = models.BooleanField()